'''
Exercício 2:
objetivo: implementar uma função que busque um valor em uma lista.

'''

def busca (elemento, lista):
    #retorna true caso elemento esteja na lista
    #retorna false caso elemento não esteja na lista
    
    for e in lista:
        if elemento == e:
            return True
    #percorremos toda a lista e não encontramos o elemento, por isso o return fora do for    
    return False

list = [1, 2, 3, 4, 5]
x = int(input("Digite o elemento a ser buscado: "))
if busca (x, list) == True:
    print (f"{x} está na lista")
else:
    print (f"{x} Não está na lista")