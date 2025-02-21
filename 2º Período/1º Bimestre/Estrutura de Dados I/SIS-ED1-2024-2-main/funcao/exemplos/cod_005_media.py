# funcao que recebe parametro e devolve valor
def calcula_media(v):
    """
    Calcular a media dos valores de uma lista
    """
    soma = 0
    for e in v:
        soma += e
    # fim do for
    media = soma/len(v)
    return media
    
resultado = calcula_media([10.5,20.1,30.4,40])
print(resultado)
idades = calcula_media([18,19,21,17,25,30])
print(idades)