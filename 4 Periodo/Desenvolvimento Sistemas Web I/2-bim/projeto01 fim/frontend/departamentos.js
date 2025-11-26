const BASE_URL = "http://localhost:8000";

let cachedDepartamentos = [];

async function fetchDepartamentos(){
    const res = await fetch(`${BASE_URL}/v1/Departamento/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedDepartamentos = data;
    return data;
}

function debounce(fn, wait){ let t; return (...a)=>{ clearTimeout(t); t = setTimeout(()=> fn.apply(this,a), wait); }; }

function renderDepartamentosList(items){
    const tbody = document.querySelector('#departamentos-table tbody');
    tbody.innerHTML = '';
    items.forEach(d=>{
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${d.id}</td><td>${d.nome}</td><td>${d.descricao}</td><td></td>`;
        tbody.appendChild(tr);
    });

    // adicionar botões
    const rows = document.querySelectorAll('#departamentos-table tbody tr');
    rows.forEach((r, idx)=>{
        const id = items[idx].id;
        const cell = r.querySelector('td:last-child');
        cell.innerHTML = ` <button class='btn btn-sm btn-primary edit' data-id='${id}'>Editar</button> <button class='btn btn-sm btn-danger del' data-id='${id}'>Del</button>`;
    });

    document.querySelectorAll('.edit').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const item = items.find(x => String(x.id) === String(id));
        if (!item) return;
        document.getElementById('d_id').value = item.id;
        document.getElementById('d_nome').value = item.nome || '';
        document.getElementById('d_descricao').value = item.descricao || '';
        document.getElementById('d_submit').textContent = 'Salvar';
    }));

    document.querySelectorAll('.del').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const itemName = items.find(x => String(x.id) === String(id))?.nome || '#' + id;
        const ok = await window.confirmAction(`Tem certeza que deseja deletar o departamento "${itemName}"? Esta ação não pode ser desfeita.`);
        if (!ok) return;
        const res = await fetch(`${BASE_URL}/v1/Departamento/${id}`, { method: 'DELETE' });
        if (res.ok) { showAlert('Departamento deletado com sucesso!', 'success'); await loadAndRenderDepartamentos(); } else { showAlert('Erro ao deletar o departamento', 'danger'); }
    }));
}

document.getElementById('form-dep').addEventListener('submit', async (ev)=>{
    ev.preventDefault();
    const id = String(document.getElementById('d_id').value).trim();
    const payload = { nome: document.getElementById('d_nome').value.trim(), descricao: document.getElementById('d_descricao').value.trim() };
    let res;
    if (id && id !== '') {
        res = await fetch(`${BASE_URL}/v1/Departamento/${id}`, { method: 'PUT', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    } else {
        res = await fetch(`${BASE_URL}/v1/Departamento/`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    }
    if (res.ok) { showAlert(id ? 'Departamento atualizado com sucesso!' : 'Departamento criado com sucesso!', 'success'); document.getElementById('form-dep').reset(); document.getElementById('d_submit').textContent = 'Criar'; await loadAndRenderDepartamentos(); } else { const t = await res.text(); showAlert('Erro ao salvar departamento: ' + t, 'danger'); }
});

document.getElementById('d_cancel').addEventListener('click', ()=>{
    document.getElementById('form-dep').reset();
    document.getElementById('d_id').value = '';
    document.getElementById('d_submit').textContent = 'Criar';
});

async function loadAndRenderDepartamentos(){
    await fetchDepartamentos();
    renderDepartamentosList(cachedDepartamentos);
}

async function init(){
    await loadAndRenderDepartamentos();
    const input = document.getElementById('search-deps');
    const handler = debounce((ev)=>{
        const q = (ev.target.value||'').toLowerCase().trim();
        if (!q) return renderDepartamentosList(cachedDepartamentos);
        const filtered = cachedDepartamentos.filter(d => (d.nome||'').toLowerCase().includes(q));
        renderDepartamentosList(filtered);
    }, 200);
    if (input) input.addEventListener('input', handler);
}

init();
