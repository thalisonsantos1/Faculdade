"""
Exercício 2: Função de Busca
Objetivo:
Implementar uma função que busque um valor em uma lista
"""
def busca(elemento, lista):
    # retornar true caso elemento esteja na lista
    # retornar false caso elemento nao esteja na lista
    for e in lista:
        if elemento == e:
            return True
    # percorremos toda a lista e nao encontramos o elemento
    return False

list = [3,8,5,4]
x = int(input("Digite elemento: "))
if busca(x, list) == True:
    print(f"{x} esta na lista")
else:
    print(f"{x} NAO esta na lista")