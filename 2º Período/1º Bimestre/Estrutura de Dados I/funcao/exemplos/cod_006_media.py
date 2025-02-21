#função que recebe parametro e devolve valor
'''
Calcular valores de uma lista

'''

def calcula_media (v):
    if len (v) > 0:
        media = sum (v) / len (v)
        return media
    else: 
        return "A lista está vazia. A Média é zero!"

resultado = calcula_media ([10, 20, 30, 40])
print (resultado)