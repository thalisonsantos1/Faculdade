# funcao que recebe parametro e devolve valor
def calcula_media(v):
    if len(v) > 0:
        media = sum(v)/len(v)
        return media
    else:
        return 0
    
resultado = calcula_media([10.5,20.1,30.4,40])
print(resultado)
idades = calcula_media([18,19,21,17,25,30])
print(idades)
teste = calcula_media([])
print(teste)