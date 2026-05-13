let usuarioEmEdicao = null;
let usuarioParaDelete = null;
let deleteModal = null;

function mostrarAlerta(mensagem, tipo = 'success') {
    const alertContainer = document.getElementById('alertContainer');
    const alertHtml = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${mensagem}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    alertContainer.innerHTML = alertHtml;
    setTimeout(() => {
        alertContainer.innerHTML = '';
    }, 4000);
}

function novo() {
    usuarioEmEdicao = null;
    document.getElementById('formTitle').textContent = 'Nova Pessoa';
    document.getElementById('conteudo').style.display = 'none';
    document.getElementById('formulario').style.display = 'block';
    document.getElementById('nameInput').value = '';
    document.getElementById('phoneInput').value = '';
    document.getElementById('emailInput').value = '';
    document.getElementById('nameInput').focus();
}

function cancelar() {
    usuarioEmEdicao = null;
    document.getElementById('conteudo').style.display = 'block';
    document.getElementById('formulario').style.display = 'none';
    document.getElementById('nameInput').value = '';
    document.getElementById('phoneInput').value = '';
    document.getElementById('emailInput').value = '';
}

function salvar() {
    if (usuarioEmEdicao) {
        alterar();
    } else {
        inserir();
    }
}

function normalizeResponseData(json) {
    if (Array.isArray(json)) {
        return json;
    }
    if (json && Array.isArray(json.users)) {
        return json.users;
    }
    if (json && Array.isArray(json.data)) {
        return json.data;
    }
    return [];
}

async function listar() {
    document.getElementById('conteudo').innerHTML = `
        <div class="card-body text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Carregando...</span>
            </div>
            <p class="mt-2">Carregando pessoas...</p>
        </div>
    `;

    try {
        const resp = await fetch('/users');
        if (!resp.ok) {
            throw new Error(`Erro ao listar: ${resp.status}`);
        }

        const json = await resp.json();
        const dados = normalizeResponseData(json);

        let rows = '';
        if (dados.length === 0) {
            rows = `
                <tr>
                    <td colspan="5" class="text-center py-4 text-muted">Nenhuma pessoa cadastrada</td>
                </tr>
            `;
        } else {
            dados.forEach(item => {
                const id = item.idusuario ?? '-';
                const nome = item.nome || '-';
                const telefone = item.telefone || '-';
                const email = item.email || '-';
                const nomeEscaped = String(nome).replace(/'/g, "\\'");

                rows += `
                    <tr>
                        <td>${id}</td>
                        <td>${nome}</td>
                        <td>${telefone}</td>
                        <td>${email}</td>
                        <td>
                            <button class="btn btn-sm btn-info me-2" onclick="editar(${id})">
                                <i class="bi bi-pencil"></i> Editar
                            </button>
                            <button class="btn btn-sm btn-danger" onclick="confirmarDelecao(${id}, '${nomeEscaped}')">
                                <i class="bi bi-trash"></i> Deletar
                            </button>
                        </td>
                    </tr>
                `;
            });
        }

        const tabela = `
            <div class="table-responsive">
                <table class="table table-striped table-hover mb-0">
                    <thead class="table-dark">
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Telefone</th>
                            <th>Email</th>
                            <th>Ações</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${rows}
                    </tbody>
                </table>
            </div>
        `;

        document.getElementById('conteudo').innerHTML = tabela;
    } catch (error) {
        console.error('Erro completo:', error);
        mostrarAlerta('Erro ao carregar pessoas: ' + error.message, 'danger');
        document.getElementById('conteudo').innerHTML = `
            <div class="card-body text-center">
                <p class="text-danger"><strong>Erro:</strong> ${error.message}</p>
            </div>
        `;
    }
}

async function editar(id) {
    try {
        const resp = await fetch(`/users/${id}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });

        if (!resp.ok) {
            throw new Error(`Erro ao buscar pessoa: ${resp.status}`);
        }

        const pessoa = await resp.json();
        usuarioEmEdicao = pessoa;
        document.getElementById('formTitle').textContent = `Editando: ${pessoa.nome}`;
        document.getElementById('nameInput').value = pessoa.nome || '';
        document.getElementById('phoneInput').value = pessoa.telefone || '';
        document.getElementById('emailInput').value = pessoa.email || '';
        document.getElementById('conteudo').style.display = 'none';
        document.getElementById('formulario').style.display = 'block';
        document.getElementById('nameInput').focus();
    } catch (error) {
        console.error('Erro:', error);
        mostrarAlerta('Erro ao buscar pessoa: ' + error.message, 'danger');
    }
}

async function alterar() {
    try {
        const nome = document.getElementById('nameInput').value;
        const telefone = document.getElementById('phoneInput').value;
        const email = document.getElementById('emailInput').value;

        if (!nome || !telefone || !email) {
            mostrarAlerta('Todos os campos são obrigatórios', 'warning');
            return;
        }

        const atualizar = { nome, telefone, email };
        const resp = await fetch(`/users/${usuarioEmEdicao.idusuario}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(atualizar)
        });

        if (!resp.ok) {
            throw new Error(`Erro ao atualizar: ${resp.status}`);
        }

        document.getElementById('conteudo').style.display = 'block';
        document.getElementById('formulario').style.display = 'none';
        usuarioEmEdicao = null;
        mostrarAlerta('Pessoa atualizada com sucesso!', 'success');
        listar();
    } catch (error) {
        console.error('Erro:', error);
        mostrarAlerta('Erro ao atualizar: ' + error.message, 'danger');
    }
}

async function inserir() {
    try {
        const nome = document.getElementById('nameInput').value;
        const telefone = document.getElementById('phoneInput').value;
        const email = document.getElementById('emailInput').value;

        if (!nome || !telefone || !email) {
            mostrarAlerta('Todos os campos são obrigatórios', 'warning');
            return;
        }

        const novo = { nome, telefone, email };
        const resp = await fetch('/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(novo)
        });

        if (!resp.ok) {
            throw new Error(`Erro ao inserir: ${resp.status}`);
        }

        document.getElementById('conteudo').style.display = 'block';
        document.getElementById('formulario').style.display = 'none';
        document.getElementById('nameInput').value = '';
        document.getElementById('phoneInput').value = '';
        document.getElementById('emailInput').value = '';
        mostrarAlerta('Pessoa inserida com sucesso!', 'success');
        listar();
    } catch (error) {
        console.error('Erro:', error);
        mostrarAlerta('Erro ao inserir: ' + error.message, 'danger');
    }
}

function confirmarDelecao(id, nome) {
    usuarioParaDelete = id;
    document.getElementById('nomeToDelete').textContent = nome;
    if (deleteModal) {
        deleteModal.show();
    }
}

async function confirmarDelete() {
    if (!usuarioParaDelete) return;

    try {
        const resp = await fetch(`/users/${usuarioParaDelete}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });

        if (!resp.ok) {
            throw new Error(`Erro ao deletar: ${resp.status}`);
        }

        if (deleteModal) {
            deleteModal.hide();
        }

        usuarioParaDelete = null;
        mostrarAlerta('Pessoa deletada com sucesso!', 'success');
        listar();
    } catch (error) {
        console.error('Erro:', error);
        mostrarAlerta('Erro ao deletar: ' + error.message, 'danger');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    deleteModal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'));
    document.getElementById('searchInput').addEventListener('input', function(event) {
        const searchTerm = event.target.value.trim().toLowerCase();
        if (!searchTerm) {
            listar();
            return;
        }

        const rows = Array.from(document.querySelectorAll('#conteudo tbody tr'));
        rows.forEach(row => {
            const texto = row.innerText.toLowerCase();
            row.style.display = texto.includes(searchTerm) ? '' : 'none';
        });
    });

    listar();
});
