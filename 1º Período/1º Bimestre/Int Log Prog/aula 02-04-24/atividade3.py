'''
Verifique se um aluno foi aprovado em uma disciplina com média igual ou superior a 7.0 e frequencia igual ou superior a 75%
'''

media = float(input("Digite a média do aluno: "))
frequencia = float(input("Informe a porcentagem de frequência do aluno: "))
if media >= 7.0 and frequencia >= 75:
    print (f"Aluno aprovado!!!")
else: 
    print (f"Aluno reprovado!!")
    