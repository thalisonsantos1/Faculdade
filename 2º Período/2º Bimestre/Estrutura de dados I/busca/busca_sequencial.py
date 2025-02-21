import requests

url_base = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/"
#nome_procurado deve ser minusculo e sem acentos
nome_procurado = input("Qual nome deseja pesquisar? ")
url_busca = url_base + nome_procurado

response = requests.get (url_busca)
print(response.text)