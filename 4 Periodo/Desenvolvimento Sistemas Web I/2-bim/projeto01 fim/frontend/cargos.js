const BASE_URL = "http://localhost:8000";

let cachedDepartamentos = [];
let cachedCargos = [];

async function fetchDepartamentos(){
    const res = await fetch(`${BASE_URL}/v1/Departamento/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedDepartamentos = data;
    return data;
}

function getDepartamentoName(id){
    if (!id) return '';
    const d = cachedDepartamentos.find(x => String(x.id) === String(id));
    return d ? d.nome : id;
}

async function fetchCargos(){
    const res = await fetch(`${BASE_URL}/v1/Cargo/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedCargos = data;
    return data;
}

function debounce(fn, wait){ let t; return (...a)=>{ clearTimeout(t); t = setTimeout(()=> fn.apply(this,a), wait); }; }

function formatCurrencyBRL(value){
    if (value === null || value === undefined || value === '') return '';
    const n = Number(value);
    if (isNaN(n)) return value;
    return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(n);
}

function renderCargosList(items){
    const tbody = document.querySelector('#cargos-table tbody');
    tbody.innerHTML = '';
    items.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${c.id}</td>
            <td>${c.nome}</td>
            <td>${formatCurrencyBRL(c.salario)}</td>
            <td>${getDepartamentoName(c.departamento_id) ?? ''}</td>
            <td>
                <button class="btn btn-sm btn-primary btn-edit" data-id="${c.id}">Editar</button>
                <button class="btn btn-sm btn-danger btn-del" data-id="${c.id}">Deletar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });

    document.querySelectorAll('.btn-edit').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const item = (cachedCargos || []).find(x => String(x.id) === String(id));
        if (!item) return;
        document.getElementById('c_id').value = item.id;
        document.getElementById('c_nome').value = item.nome || '';
        document.getElementById('c_salario').value = item.salario ?? '';
        document.getElementById('c_descricao').value = item.descricao || '';
        document.getElementById('c_departamento').value = item.departamento_id ?? '';
        document.getElementById('c_submit').textContent = 'Salvar';
    }));

    document.querySelectorAll('.btn-del').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const itemName = cachedCargos.find(x => String(x.id) === String(id))?.nome || '#' + id;
        const ok = await window.confirmAction(`Tem certeza que deseja deletar o cargo "${itemName}"? Esta ação não pode ser desfeita.`);
        if (!ok) return;
        const res = await fetch(`${BASE_URL}/v1/Cargo/${id}`, { method: 'DELETE' });
        if (res.ok) { showAlert('Cargo deletado com sucesso!', 'success'); await loadAndRenderCargos(); } else { showAlert('Erro ao deletar o cargo', 'danger'); }
    }));
}

async function populateDepartamentos(){
    const deps = await fetchDepartamentos();
    const sel = document.getElementById('c_departamento');
    sel.innerHTML = '<option value="">Escolha</option>';
    deps.forEach(d=>{
        const o = document.createElement('option'); o.value = d.id; o.textContent = d.nome; sel.appendChild(o);
    });
}

document.getElementById('form-cargo').addEventListener('submit', async (ev)=>{
    ev.preventDefault();
    const id = String(document.getElementById('c_id').value).trim();
    const payload = {
        nome: document.getElementById('c_nome').value.trim(),
        salario: parseFloat(document.getElementById('c_salario').value),
        descricao: document.getElementById('c_descricao').value.trim(),
        departamento_id: parseInt(document.getElementById('c_departamento').value)
    };
    let res;
    if (id && id !== '') {
        res = await fetch(`${BASE_URL}/v1/Cargo/${id}`, { method: 'PUT', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    } else {
        res = await fetch(`${BASE_URL}/v1/Cargo/`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    }
    if (res.ok) { showAlert(id ? 'Cargo atualizado com sucesso!' : 'Cargo criado com sucesso!', 'success'); document.getElementById('form-cargo').reset(); document.getElementById('c_submit').textContent = 'Criar Cargo'; await loadAndRenderCargos(); } else { const t = await res.text(); showAlert('Erro ao salvar cargo: ' + t, 'danger'); }
});

document.getElementById('c_cancel').addEventListener('click', ()=>{
    document.getElementById('form-cargo').reset();
    document.getElementById('c_id').value = '';
    document.getElementById('c_submit').textContent = 'Criar Cargo';
});

async function loadAndRenderCargos(){
    await fetchCargos();
    renderCargosList(cachedCargos);
}

async function initCargos(){
    await populateDepartamentos();
    await loadAndRenderCargos();
    const input = document.getElementById('search-cargos');
    const handler = debounce((ev)=>{
        const q = (ev.target.value||'').toLowerCase().trim();
        if (!q) return renderCargosList(cachedCargos);
        const filtered = cachedCargos.filter(c => (c.nome||'').toLowerCase().includes(q));
        renderCargosList(filtered);
    }, 200);
    if (input) input.addEventListener('input', handler);
}

initCargos();
