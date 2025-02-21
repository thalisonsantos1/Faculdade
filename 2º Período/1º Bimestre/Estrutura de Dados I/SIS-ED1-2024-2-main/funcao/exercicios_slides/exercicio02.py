
# criar uma funcao que receba a nota e devolver o status conforme enunciado.
"""
Faça uma função que informe o status do aluno a
partir da sua média de acordo com a tabela a seguir:
 Nota acima de 6 à 'Aprovado'
 Nota entre 4 e 6 à 'Verificação Suplementar'
 Nota abaixo de 4 à 'Reprovado'
"""
def status(nota):
    if nota >= 6:
        return "Aprovado"
    elif nota >= 4:
        return "Verificação Suplementar"
    else:
        return "Reprovado"
def lista_notas(notas):
    for nota in notas:
        res =  status(nota)
        print(f"Nota: {nota} - {res}")
# uma lista com as notas
notas = [5, 7.5, 8.3, 9, 3, 4]
lista_notas(notas)