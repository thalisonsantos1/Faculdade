const BASE_URL = "http://localhost:8000";

let cachedCargos = [];
let cachedFuncionarios = [];

async function fetchCargos() {
    const res = await fetch(`${BASE_URL}/v1/Cargo/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedCargos = data;
    return data;
}

function getCargoName(id){
    if (!id) return '';
    const c = cachedCargos.find(x => String(x.id) === String(id));
    return c ? c.nome : id;
}

async function fetchFuncionarios() {
    const res = await fetch(`${BASE_URL}/v1/Funcionario/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedFuncionarios = data;
    return data;
}

function showMessage(text, type = 'success'){
    if (window.showAlert) return window.showAlert(text, type);
    const div = document.getElementById('msg');
    div.innerHTML = `<div class="alert alert-${type} alert-sm">${text}</div>`;
    setTimeout(()=> div.innerHTML = '', 3000);
}

async function renderCargos(){
    const cargos = await fetchCargos();
    const select = document.getElementById('cargo_id');
    const lista = document.getElementById('lista-cargos');
    select.innerHTML = '<option value="">Escolha um cargo</option>';
    lista.innerHTML = '';
    cargos.forEach(c => {
        const opt = document.createElement('option');
        opt.value = c.id;
        opt.textContent = c.nome;
        select.appendChild(opt);

        const li = document.createElement('li');
        li.className = 'list-group-item d-flex justify-content-between align-items-center';
        li.textContent = c.nome;
        lista.appendChild(li);
    });
}

function debounce(fn, wait){
    let t;
    return (...args) => { clearTimeout(t); t = setTimeout(()=> fn.apply(this, args), wait); };
}

function renderFuncionariosList(funcionarios){
    const tbody = document.querySelector('#funcionarios-table tbody');
    tbody.innerHTML = '';
    funcionarios.forEach(f => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${f.id}</td>
            <td>${f.nome}</td>
            <td>${getCargoName(f.cargo_id) ?? ''}</td>
            <td>
                <button class="btn btn-sm btn-primary btn-edit" data-id="${f.id}">Editar</button>
                <button class="btn btn-sm btn-danger btn-delete" data-id="${f.id}">Deletar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });

    document.querySelectorAll('.btn-edit').forEach(b => b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const f = funcionarios.find(x => String(x.id) === String(id));
        if (!f) return;
        document.getElementById('f_id').value = f.id;
        document.getElementById('nome').value = f.nome;
        document.getElementById('cargo_id').value = f.cargo_id || '';
        document.getElementById('f_submit').textContent = 'Salvar';
    }));

    document.querySelectorAll('.btn-delete').forEach(b => b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const ok = window.confirmAction ? await window.confirmAction('Deletar funcionário #' + id + '?') : confirm('Deletar funcionário #' + id + '?');
        if (!ok) return;
        const res = await fetch(`${BASE_URL}/v1/Funcionario/${id}`, { method: 'DELETE' });
        if (res.ok) {
            showAlert('Funcionário deletado com sucesso!', 'success');
            await loadAndRenderFuncionarios();
        } else {
            showAlert('Erro ao deletar funcionário', 'danger');
        }
    }));
}

async function renderFuncionarios(){
    const funcionarios = await fetchFuncionarios();
    renderFuncionariosList(funcionarios);
}

async function loadAndRenderFuncionarios(){
    await fetchFuncionarios();
    renderFuncionariosList(cachedFuncionarios);
}

document.getElementById('form-add').addEventListener('submit', async (ev)=>{
    ev.preventDefault();
    const id = String(document.getElementById('f_id').value).trim();
    const nome = document.getElementById('nome').value.trim();
    const cargo_id = parseInt(document.getElementById('cargo_id').value);
    if (!nome || !cargo_id) { showAlert('Por favor, preencha Nome e Cargo', 'warning'); return; }

    const payload = { nome, cargo_id };
    let res;
    if (id && id !== '') {
        res = await fetch(`${BASE_URL}/v1/Funcionario/${id}`, {
            method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
        });
    } else {
        res = await fetch(`${BASE_URL}/v1/Funcionario/`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    }

    if (res.ok) {
        showAlert(id ? 'Funcionário atualizado com sucesso!' : 'Funcionário criado com sucesso!', 'success');
        document.getElementById('form-add').reset();
        document.getElementById('f_submit').textContent = 'Criar';
        await loadAndRenderFuncionarios();
    } else {
        const txt = await res.text();
        showAlert('Erro ao salvar funcionário: ' + txt, 'danger');
    }
});

document.getElementById('f_cancel').addEventListener('click', ()=>{
    document.getElementById('form-add').reset();
    document.getElementById('f_id').value = '';
    document.getElementById('f_submit').textContent = 'Criar';
});

async function init(){
    await renderCargos();
    await loadAndRenderFuncionarios();

    const input = document.getElementById('search-func');
    const doFilter = debounce((ev)=>{
        const q = (ev.target.value || '').toLowerCase().trim();
        if (!q) return renderFuncionariosList(cachedFuncionarios);
        const filtered = cachedFuncionarios.filter(f => (f.nome || '').toLowerCase().includes(q));
        renderFuncionariosList(filtered);
    }, 200);
    if (input) input.addEventListener('input', doFilter);
}

init();
