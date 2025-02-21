async function getDados() {
    // faz a chamada do endpoint Flask
    const response = await fetch('http://127.0.0.1:5000/soma');

    // verificar se a resposta foi bem sucedida
    if (response.ok) {
        // tratar o conteúdo da resposta
        const dados = await response.text();
        console.log(dados)
        document.getElementById("exit").textContent = dados
    }
}

async function buscaCliente() {
    const doc_cpf = document.getElementById("doc").value;
    if (!doc_cpf){
        alert("Informe o CPF")
        return;
    }
    //devemos tratar erros!
    const response = await fetch(`http://127.0.0.1:5000/consulta?doc=${doc_cpf}`);
    const dados = await response.json();
    console.log(dados);
    document.getElementById('nome').textContent = dados.nome;
    document.getElementById('nascimento').textContent = dados.data_nascimento;
    document.getElementById('email').textContent = dados.email;
}

async function cadastrarCliente() {
    //pegando os dados inseridos no HTML

    const cpf = document.getElementById("cpf-cadastro").value;
    const nome = document.getElementById("name").value;
    const data_nascimento = document.getElementById("data_nascimento").value;
    const email = document.getElementById("mail").value;


    //criando a estrutura que definimos para o json
    const payload = {
        cpf,
        dados: {
            nome,
            data_nascimento,
            email,
        }
    };
    //fazendo a requisição no backend
    const response = await fetch('http://127.0.0.1:5000/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    // consultando se já existe um cadastro no json com o mesmo CPF e emitindo um alert
    const retorno = await response.json();
    if (retorno) {        
        alert("CPF duplicado");
    }else{
        alert("Cadastro efetuado com sucesso");
    }
     
}