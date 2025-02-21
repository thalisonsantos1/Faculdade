"""Exercício 1: Função de Soma de Elementos
Objetivo:
Implementar uma função que calcule a soma dos elementos de uma lista."""
def soma(lista):
    s = 0
    for elemento in lista:
        s += elemento
    return s

a = [10,20,30,40,50]
x = soma(a)
print(f"a soma eh {x}")
