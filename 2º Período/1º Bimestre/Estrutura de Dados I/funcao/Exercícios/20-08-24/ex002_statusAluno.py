#criar uma função que receba a nota e devolver o status conforme o enunciado.
    # --> nota acima de 6: Aprovado
    # --> nota entre 4 e 6: Verificação Suplementar
    # --> nota abaixo de 4: Reprovado
'''
notas = [5, 7.5, 8.3, 9, 3, 4]
def media_final(notas): 
    for i in notas:
        if i >= 6:
            resultado = "aprovado"
            print (resultado)
        if i >= 4 and i < 6:
            resultado = "Verficação Suplementar"
            print (resultado)
        if i < 4:
            resultado = "Reprovado"
            print (resultado)
    return
            
situacao = media_final (notas) '''




#lista com as notas
notas = [5, 7.5, 8.3, 9, 3, 4]

#resolução Alysson:

def status (nota):
    if nota >= 6:
        return "Aprovado"
    elif nota >= 4:
        return "Verificação suplementar"
    else: 
        return "Reprovado"
    
notas = [5, 7.5, 8.3, 9, 3, 4]

for nota in notas:
    res = status (nota)
    print (f"Nota: {nota} - {res}")