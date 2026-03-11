

listar();

function novo() {
    document.getElementById("conteuudo").style.display = "none";
    document.getElementById("formulario").style.display = "block";
    document.getElementById("txtnome").value = "";
    document.getElementById("txttelefone").value = "";
}



async function listar() {
    document.getElementById("conteudo").innerHTML = "aguarde....";

    const resp = await fetch("/pessoa", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (!resp.ok) {
        console.log("erro" + resp.status);
    }

    //see fosse JSON, converte a resposta para JSON
    const dados = await resp.json();
    let tabela =   `<table width = '100%' border = '1'>
                    <th>Nome</th>
                    <th>Telefone</th>
                    `;

    for (let i = 0; i < dados.length; i++) {
        tabela += `<tr>
                    <td>${dados[i].nome}</td>
                    <td>${dados[i].telefone}</td>
                    </tr>`;
    }

    tabela += `</table>`;

    document.getElementById("conteudo").innerHTML = tabela;
}

async function consultar() {
    document.getElementById("conteudo").innerHTML = "aguarde....";

    const resp = await fetch("/pessoa/222", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (!resp.ok) {
        console.log("erro" + resp.status);
    }

    //see fosse JSON, converte a resposta para JSON
    //const dados = await resp.json();

    const retorno = await resp.text();
    document.getElementById("conteudo").innerHTML = retorno;
}

async function inserir() {
    document.getElementById("conteudo").innerHTML = "aguarde....";

    const novo = {
        nome: "Bill Gates",
        email: "bill@microsoft.com"
    }

    const resp = await fetch("/pessoa", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(novo)
    });

    if (!resp.ok) {
        console.log("erro" + resp.status);
    }

    //see fosse JSON, converte a resposta para JSON
    //const dados = await resp.json();
    const retorno = await resp.text();
 
    document.getElementById("conteudo").innerHTML = retorno;
    
}

async function alterar() {
    document.getElementById("conteudo").innerHTML = "aguarde....";

    const dados = {
        nome: "Bill Gates",
        email: "bill@microsoft.com"
    }

    const resp = await fetch("/pessoa/123", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    if (!resp.ok) {
        console.log("erro" + resp.status);
    }

    //see fosse JSON, converte a resposta para JSON
    //const dados = await resp.json();
    const retorno = await resp.text(); 
    document.getElementById("conteudo").innerHTML = retorno;
    
}

async function excluir() {
    document.getElementById("conteudo").innerHTML = "aguarde....";

    const resp = await fetch("/pessoa/123", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    if (!resp.ok) {
        console.log("erro" + resp.status);
    }

    //see fosse JSON, converte a resposta para JSON
    //const dados = await resp.json();
    const retorno = await resp.text();
    document.getElementById("conteudo").innerHTML = retorno;
}


