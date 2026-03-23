let pessoaEmEdicao = null;
let pessoaParaDelete = null;

// Aguardar o DOM estar pronto
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM carregado, iniciando listar()");
    listar();
});

function novo() {
    pessoaEmEdicao = null;
    document.getElementById("formTitle").textContent = "Nova Pessoa";
    document.getElementById("conteudo").style.display = "none";
    document.getElementById("formulario").style.display = "block";
    document.getElementById("txtnome").value = "";
    document.getElementById("txttelefone").value = "";
    document.getElementById("txtemail").value = "";
}

function cancelar() {
    pessoaEmEdicao = null;
    document.getElementById("conteudo").style.display = "block";
    document.getElementById("formulario").style.display = "none";
    document.getElementById("txtnome").value = "";
    document.getElementById("txttelefone").value = "";
    document.getElementById("txtemail").value = "";
}

function salvar() {
    if (pessoaEmEdicao) {
        alterar();
    } else {
        inserir();
    }
}

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

async function listar() {
    console.log("listar() iniciado");
    document.getElementById("conteudo").innerHTML = `
        <div class="card-body text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Carregando...</span>
            </div>
            <p class="mt-2">Carregando pessoas...</p>
        </div>
    `;

    try {
        console.log("Fazendo requisição GET para /pessoa");
        const resp = await fetch("/pessoa", {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        console.log("Resposta recebida:", resp.status);

        if (!resp.ok) {
            throw new Error(`Erro ao listar: ${resp.status}`);
        }

        const dados = await resp.json();
        console.log("Dados recebidos:", dados);
        
        if (dados.length === 0) {
            document.getElementById("conteudo").innerHTML = `
                <div class="card-body text-center">
                    <p class="text-muted">Nenhuma pessoa cadastrada</p>
                </div>
            `;
            return;
        }

        let tabela = `
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
        `;
        
        for (let i = 0; i < dados.length; i++) {
            tabela += `
                <tr>
                    <td>${dados[i].idpessoa}</td>
                    <td>${dados[i].nome}</td>
                    <td>${dados[i].telefone}</td>
                    <td>${dados[i].email}</td>
                    <td>
                        <button class="btn btn-sm btn-info" onclick="editar(${dados[i].idpessoa})">
                            <i class="bi bi-pencil"></i> Editar
                        </button>
                        <button class="btn btn-sm btn-danger" onclick="confirmarDelecao(${dados[i].idpessoa}, '${dados[i].nome}')">
                            <i class="bi bi-trash"></i> Deletar
                        </button>
                    </td>
                </tr>
            `;
        }
        
        tabela += `
                    </tbody>
                </table>
            </div>
        `;

        console.log("Tabela construída, atualizando DOM");
        document.getElementById("conteudo").innerHTML = tabela;
        console.log("Tabela atualizada com sucesso");
    } catch (error) {
        console.error("Erro completo:", error);
        console.error("Stack trace:", error.stack);
        mostrarAlerta('Erro ao carregar pessoas: ' + error.message, 'danger');
        document.getElementById("conteudo").innerHTML = `
            <div class="card-body text-center">
                <p class="text-danger"><strong>Erro:</strong> ${error.message}</p>
            </div>
        `;
    }
}

async function editar(id) {
    try {
        const resp = await fetch(`/pessoa/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!resp.ok) {
            throw new Error(`Erro ao buscar pessoa: ${resp.status}`);
        }

        const pessoa = await resp.json();
        
        pessoaEmEdicao = pessoa;
        document.getElementById("formTitle").textContent = `Editando: ${pessoa.nome}`;
        document.getElementById("txtnome").value = pessoa.nome;
        document.getElementById("txttelefone").value = pessoa.telefone;
        document.getElementById("txtemail").value = pessoa.email;
        
        document.getElementById("conteudo").style.display = "none";
        document.getElementById("formulario").style.display = "block";
        document.getElementById("txtnome").focus();
    } catch (error) {
        console.error("Erro:", error);
        mostrarAlerta('Erro ao buscar pessoa: ' + error.message, 'danger');
    }
}

async function alterar() {
    try {
        const nome = document.getElementById("txtnome").value;
        const telefone = document.getElementById("txttelefone").value;
        const email = document.getElementById("txtemail").value;

        if (!nome || !telefone || !email) {
            mostrarAlerta('Todos os campos são obrigatórios', 'warning');
            return;
        }

        const atualizar = {
            nome: nome,
            telefone: telefone,
            email: email
        };

        const resp = await fetch(`/pessoa/${pessoaEmEdicao.idpessoa}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(atualizar)
        });

        if (!resp.ok) {
            throw new Error(`Erro ao atualizar: ${resp.status}`);
        }

        const resultado = await resp.json();
        
        document.getElementById("conteudo").style.display = "block";
        document.getElementById("formulario").style.display = "none";
        pessoaEmEdicao = null;
        
        mostrarAlerta('Pessoa atualizada com sucesso!', 'success');
        listar();
    } catch (error) {
        console.error("Erro:", error);
        mostrarAlerta('Erro ao atualizar: ' + error.message, 'danger');
    }
}

async function inserir() {
    try {
        const nome = document.getElementById("txtnome").value;
        const telefone = document.getElementById("txttelefone").value;
        const email = document.getElementById("txtemail").value;

        if (!nome || !telefone || !email) {
            mostrarAlerta('Todos os campos são obrigatórios', 'warning');
            return;
        }

        const novo = {
            nome: nome,
            telefone: telefone,
            email: email
        };

        const resp = await fetch("/pessoa", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(novo)
        });

        if (!resp.ok) {
            throw new Error(`Erro ao inserir: ${resp.status}`);
        }

        const resultado = await resp.json();

        document.getElementById("conteudo").style.display = "block";
        document.getElementById("formulario").style.display = "none";
        document.getElementById("txtnome").value = "";
        document.getElementById("txttelefone").value = "";
        document.getElementById("txtemail").value = "";

        mostrarAlerta('Pessoa inserida com sucesso!', 'success');
        listar();
    } catch (error) {
        console.error("Erro:", error);
        mostrarAlerta('Erro ao inserir: ' + error.message, 'danger');
    }
}

function confirmarDelecao(id, nome) {
    pessoaParaDelete = id;
    document.getElementById("nomeToDelete").textContent = nome;
    
    const modal = new bootstrap.Modal(document.getElementById("confirmDeleteModal"));
    modal.show();
}

async function confirmarDelete() {
    if (!pessoaParaDelete) return;

    try {
        const resp = await fetch(`/pessoa/${pessoaParaDelete}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!resp.ok) {
            throw new Error(`Erro ao deletar: ${resp.status}`);
        }

        const resultado = await resp.json();
        
        const modal = bootstrap.Modal.getInstance(document.getElementById("confirmDeleteModal"));
        modal.hide();
        
        pessoaParaDelete = null;
        mostrarAlerta('Pessoa deletada com sucesso!', 'success');
        listar();
    } catch (error) {
        console.error("Erro:", error);
        mostrarAlerta('Erro ao deletar: ' + error.message, 'danger');
    }
}


