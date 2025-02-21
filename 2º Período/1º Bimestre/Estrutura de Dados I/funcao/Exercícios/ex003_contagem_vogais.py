'''
Exercício 3:
Objeto: Implementar uma função que ocnte o número de vogais em uma string

'''

def conta_vogais (texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    qtd = 0
    for letra in texto:
        if letra in vogais:
            qtd = qtd + 1
    return qtd

frase = "Ola mundo"
quantidade = conta_vogais(frase)
print (f"{frase} tem {quantidade} vogais") #acrescentar texto.lower