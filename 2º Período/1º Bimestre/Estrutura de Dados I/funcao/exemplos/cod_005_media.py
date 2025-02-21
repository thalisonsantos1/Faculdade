#função que recebe parametro e devolve valor
'''
Calcular valores de uma lista

'''

def calcula_media (v):
    soma = 0
    for i in v:
        soma += i
        #fim do for
    media = soma / len (v)
    return media

resultado = calcula_media ([10, 20, 30, 40])
print (resultado)