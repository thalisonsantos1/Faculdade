from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json

app = Flask("Minha API")

CORS(app)  # Ativa o CORS


'''@app.route("/")
def index():
    return "Hello World"


@app.route("/soma")
def soma():
    s = 0
    for i in range(10):
        s += i
    return f"resultado igual a {s}"


@app.route("/multi", methods=["GET"])
def mult():
    nome = request.args.get("nome")
    x = request.args.get("varx", type=float)
    y = request.args.get("vary")  # y será string
    y = float(y)
    resultado = x * y
    return f"Olá {nome}, o resultado da multiplicação de {x} por {y} é {resultado}" '''


@app.route("/consulta", methods=["GET"])  # 1ºINFORMA O NOME DA ROTA, 2º Métodos (opcional)
# definir função e programá-la
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    return registro

@app.route("/cadastro", methods=["POST"]) 
def cadastrar():
    payload = request.json
    cpf = payload.get("cpf")
    if consulta_duplicados(cpf): #FUNÇÃO CRIADA PARA VALIDAR CADASTRO EXISTENTE
        return jsonify(True)       
    valores = payload.get("dados")
    salvar_dados(cpf, valores)
    #ordena_json ("api-flask/dados.json") criação de uma função para ordenar os dados do Json
    return jsonify(False)

    '''valores = {
        "nome": "thalison",
        "data_nascimento": "1993-08-22",
        "email": "thalison@example.com"
    }
    salvar_dados (1111, valores)'''


def carregar_arquivo():
    #caminho de onde o arquivo está salvo
    caminho_arquivo = "api-flask/dados.json"
    try:
        with open(caminho_arquivo, "r") as arq:
            return json.load(arq)
    except Exception:
        return "Falha ao carregar o arquivo"
    
def gravar_arquivo(dados):
    caminho_arquivo = "api-flask/dados.json"
    try:
        with open(caminho_arquivo, "w") as arq:
            json.dump(dados, arq, indent=4)
            return "Dados gravados com sucesso"
    except Exception:
        return "Falha ao carregar o arquivo"
    
def salvar_dados(cpf, registro):
    dados_pessoas = carregar_arquivo()
    dados_pessoas[cpf] = registro
    gravar_arquivo(dados_pessoas)

def dados(cpf):
    dados_pessoas = carregar_arquivo()
    print (dados_pessoas)
    cliente = dados_pessoas.get(cpf, "registro não encontrado")
    return cliente

def consulta_duplicados(cpf):
    dados_pessoas = carregar_arquivo()
    return cpf in dados_pessoas.keys()
    


if __name__ == "__main__":

    app.run(debug=True)  # ativa o modo debug para salvar automaticamente alterações. é só recarregar a página
    
    
    
    
    #Pode ser uma ideia para uma rota de cadastro
    
    