const BASE_URL = "http://localhost:8000";

let cachedFuncs = [];
let cachedTreins = [];
let cachedTRs = [];

async function fetchFuncionarios(){
    const res = await fetch(`${BASE_URL}/v1/Funcionario/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedFuncs = data;
    return data;
}
async function fetchTreinamentos(){
    const res = await fetch(`${BASE_URL}/treinamentos/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedTreins = data;
    return data;
}

async function fetchTRs(){
    const res = await fetch(`${BASE_URL}/treinamentos-realizados/`);
    if (!res.ok) return [];
    const data = await res.json();
    cachedTRs = data;
    return data;
}

function formatDateBrazil(dateStr){
    if (!dateStr) return '';
    try{
        const d = new Date(dateStr);
        if (!isNaN(d)) return d.toLocaleDateString('pt-BR');
    }catch(e){}
    const parts = String(dateStr).split('T')[0].split('-');
    if (parts.length === 3) return `${parts[2]}/${parts[1]}/${parts[0]}`;
    return dateStr;
}

async function populateSelects(){
    await fetchFuncionarios();
    await fetchTreinamentos();
    const sf = document.getElementById('tr_func');
    const st = document.getElementById('tr_trein');
    sf.innerHTML = '<option value="">Escolha</option>';
    st.innerHTML = '<option value="">Escolha</option>';
    cachedFuncs.forEach(f=>{ const o=document.createElement('option'); o.value=f.id; o.textContent=`${f.nome}`; sf.appendChild(o); });
    cachedTreins.forEach(t=>{ const o=document.createElement('option'); o.value=t.id; o.textContent=`${t.nome}`; st.appendChild(o); });
}

function getFuncionarioName(id){
    const f = cachedFuncs.find(x => String(x.id) === String(id));
    return f ? f.nome : id;
}

function getTreinamentoName(id){
    const t = cachedTreins.find(x => String(x.id) === String(id));
    return t ? t.nome : id;
}

function debounce(fn, wait){ let t; return (...a)=>{ clearTimeout(t); t = setTimeout(()=> fn.apply(this,a), wait); }; }

function renderTRsList(items){
    const tbody = document.querySelector('#tr-table tbody');
    tbody.innerHTML = '';
    items.forEach(i=>{
        const tr = document.createElement('tr');
        tr.innerHTML = `<td>${i.id}</td><td>${getFuncionarioName(i.funcionario_id)}</td><td>${getTreinamentoName(i.treinamento_id)}</td><td>${formatDateBrazil(i.data_realizacao)}</td><td>${formatDateBrazil(i.data_validade)}</td><td></td>`;
        tbody.appendChild(tr);
    });
    const rows = document.querySelectorAll('#tr-table tbody tr');
    rows.forEach((r, idx)=>{
        const id = items[idx].id;
        const cell = r.querySelector('td:last-child');
        cell.innerHTML = ` <button class='btn btn-sm btn-primary edit' data-id='${id}'>Editar</button> <button class='btn btn-sm btn-danger del' data-id='${id}'>Del</button>`;
    });

    document.querySelectorAll('.edit').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const item = items.find(x => String(x.id) === String(id));
        if (!item) return;
        document.getElementById('tr_id').value = item.id;
        document.getElementById('tr_func').value = item.funcionario_id;
        document.getElementById('tr_trein').value = item.treinamento_id;
        document.getElementById('tr_data').value = String(item.data_realizacao).split('T')[0];
        document.getElementById('tr_submit').textContent = 'Salvar';
    }));

    document.querySelectorAll('.del').forEach(b=> b.addEventListener('click', async (e)=>{
        const id = e.currentTarget.dataset.id;
        const funcName = getFuncionarioName(i.funcionario_id);
        const treinName = getTreinamentoName(i.treinamento_id);
        const ok = await window.confirmAction(`Tem certeza que deseja deletar o registro do treinamento "${treinName}" realizado por "${funcName}"? Esta ação não pode ser desfeita.`);
        if (!ok) return;
        const res = await fetch(`${BASE_URL}/treinamentos-realizados/${id}`, { method: 'DELETE' });
        if (res.ok) { showAlert('Registro de treinamento deletado com sucesso!', 'success'); await loadAndRenderTRs(); } else { showAlert('Erro ao deletar o registro', 'danger'); }
    }));
}

document.getElementById('form-tr').addEventListener('submit', async (ev)=>{
    ev.preventDefault();
    const id = String(document.getElementById('tr_id').value).trim();
    const payload = {
        funcionario_id: parseInt(document.getElementById('tr_func').value),
        treinamento_id: parseInt(document.getElementById('tr_trein').value),
        data_realizacao: document.getElementById('tr_data').value || undefined
    };
    let res;
    if (id && id !== '') {
        res = await fetch(`${BASE_URL}/treinamentos-realizados/${id}`, { method: 'PUT', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ data_realizacao: payload.data_realizacao }) });
    } else {
        res = await fetch(`${BASE_URL}/treinamentos-realizados/`, { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    }
    if (res.ok) { showAlert(id ? 'Treinamento atualizado com sucesso!' : 'Treinamento registrado com sucesso!', 'success'); document.getElementById('form-tr').reset(); document.getElementById('tr_submit').textContent = 'Registrar'; await loadAndRenderTRs(); } else { const t = await res.text(); showAlert('Erro ao salvar registro: '+t, 'danger'); }
});

document.getElementById('tr_cancel').addEventListener('click', ()=>{
    document.getElementById('form-tr').reset();
    document.getElementById('tr_id').value = '';
    document.getElementById('tr_submit').textContent = 'Registrar';
});

async function loadAndRenderTRs(){
    await fetchTRs();
    renderTRsList(cachedTRs);
}

async function initTR(){
    await populateSelects();
    await loadAndRenderTRs();
    const input = document.getElementById('search-tr');
    const handler = debounce((ev)=>{
        const q = (ev.target.value||'').toLowerCase().trim();
        if (!q) return renderTRsList(cachedTRs);
        const filtered = cachedTRs.filter(r => {
            const fName = (getFuncionarioName(r.funcionario_id)||'').toLowerCase();
            const tName = (getTreinamentoName(r.treinamento_id)||'').toLowerCase();
            const d = (formatDateBrazil(r.data_realizacao)||'').toLowerCase();
            return fName.includes(q) || tName.includes(q) || d.includes(q);
        });
        renderTRsList(filtered);
    }, 200);
    if (input) input.addEventListener('input', handler);
}

initTR();

// populate footer app name if footer helper is available
if (window.footer && window.footer.setAppName) {
    try{
        const brand = document.querySelector('.navbar-brand')?.textContent || 'Gente Control- Gestão de Pessoas e Treinamentos';
        window.footer.setAppName(brand);
    }catch(e){ /* ignore */ }
}
