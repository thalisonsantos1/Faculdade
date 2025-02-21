#biblioteca que permite fazer requisições (solicitações)
import requests
import busca_sequencial2

def busca_nomes (qtd=20):
    url = f"https://gerador-nomes.wolan.net/nomes/{qtd}"
    print (url)
    resposta = requests.get(url)
    resultado = resposta.json()
    print (resposta)
    print (type(resposta))

    return resultado

def busca_ibge ():
    url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/"
    response = requests.get(url)

    print(response)
    resultado = response.json()

    lista_nomes = []

    for i in range(len(resultado)):
        elemento = resultado[i]
        nome = elemento ["nome"]
        lista_nomes.append(nome)

    return lista_nomes

if __name__ == "__main__":
    
    lista_nomes = busca_nomes()
    print (lista_nomes)
    aux = input ("Qual nome deseja pesquisar? ")
    indice = busca_sequencial2.busca_sequencial2(lista_nomes, aux)
    if indice >= 0:
        print (f"O nome {aux} foi encontrado na posicao {indice}")
    else:
        print (f"O nome {aux} nao foi encontrado")
