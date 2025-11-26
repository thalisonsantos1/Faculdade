const BASE_URL = "http://localhost:8000";

let cachedTreinamentos = [];

async function fetchTreinamentos(){
    const res = await fetch(`${BASE_URL}/treinamentos/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedTreinamentos = data;
    return data;
}

function debounce(fn, wait){ let t; return (...a)=>{ clearTimeout(t); t = setTimeout(()=> fn.apply(this,a), wait); }; }

function renderTreinamentosList(items){
    const tbody = document.querySelector('#treinamentos-table tbody');
    tbody.innerHTML = '';
    items.forEach(t=>{
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${t.id}</td><td>${t.nome}</td><td>${t.carga_horaria}</td><td>${t.validade_dias}</td><td></td>`;
        tbody.appendChild(tr);
    });

    const rows = document.querySelectorAll('#treinamentos-table tbody tr');
    rows.forEach((r, idx)=>{
        const id = items[idx].id;
        const cell = r.querySelector('td:last-child');
        cell.innerHTML = ` <button class='btn btn-sm btn-primary edit' data-id='${id}'>Editar</button> <button class='btn btn-sm btn-danger del' data-id='${id}'>Del</button>`;
    });

    document.querySelectorAll('.edit').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const item = items.find(x => String(x.id) === String(id));
        if (!item) return;
        document.getElementById('t_id').value = item.id;
        document.getElementById('t_nome').value = item.nome || '';
        document.getElementById('t_descricao').value = item.descricao || '';
        document.getElementById('t_carga').value = item.carga_horaria ?? '';
        document.getElementById('t_validade').value = item.validade_dias ?? '';
        document.getElementById('t_submit').textContent = 'Salvar';
    }));

    document.querySelectorAll('.del').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const itemName = cachedTreinamentos.find(x => String(x.id) === String(id))?.nome || '#' + id;
        const ok = await window.confirmAction(`Tem certeza que deseja deletar o treinamento "${itemName}"? Esta ação não pode ser desfeita.`);
        if (!ok) return;
        const res = await fetch(`${BASE_URL}/treinamentos/${id}`, { method: 'DELETE' });
        if (res.ok) { showAlert('Treinamento deletado com sucesso!', 'success'); await loadAndRenderTreinamentos(); } else { showAlert('Erro ao deletar o treinamento', 'danger'); }
    }));
}

document.getElementById('form-trein').addEventListener('submit', async (ev)=>{
    ev.preventDefault();
    const id = String(document.getElementById('t_id').value).trim();
    const payload = {
        nome: document.getElementById('t_nome').value.trim(),
        descricao: document.getElementById('t_descricao').value.trim(),
        carga_horaria: parseFloat(document.getElementById('t_carga').value),
        validade_dias: parseInt(document.getElementById('t_validade').value)
    };
    let res;
    if (id && id !== '') {
        res = await fetch(`${BASE_URL}/treinamentos/${id}`, { method: 'PUT', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    } else {
        res = await fetch(`${BASE_URL}/treinamentos/`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    }
    if (res.ok) { showAlert(id ? 'Treinamento atualizado com sucesso!' : 'Treinamento criado com sucesso!', 'success'); document.getElementById('form-trein').reset(); document.getElementById('t_submit').textContent = 'Criar'; await loadAndRenderTreinamentos(); } else { const t = await res.text(); showAlert('Erro ao salvar treinamento: ' + t, 'danger'); }
});

document.getElementById('t_cancel').addEventListener('click', ()=>{
    document.getElementById('form-trein').reset();
    document.getElementById('t_id').value = '';
    document.getElementById('t_submit').textContent = 'Criar';
});

async function loadAndRenderTreinamentos(){
    await fetchTreinamentos();
    renderTreinamentosList(cachedTreinamentos);
}

async function init(){
    await loadAndRenderTreinamentos();
    const input = document.getElementById('search-trein');
    const handler = debounce((ev)=>{
        const q = (ev.target.value||'').toLowerCase().trim();
        if (!q) return renderTreinamentosList(cachedTreinamentos);
        const filtered = cachedTreinamentos.filter(t => (t.nome||'').toLowerCase().includes(q));
        renderTreinamentosList(filtered);
    }, 200);
    if (input) input.addEventListener('input', handler);
}

init();
