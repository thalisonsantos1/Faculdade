'''
Eercício 1: funcção de soma dos elementos

Objetivo: implementar uma função que calcule a soma dos elementos de uma lista.

'''

def soma_elementos (v):
    soma = sum (v)
    return soma

lista = [1, 2, 3, 4, 5]
soma = soma_elementos (lista)
print (soma)