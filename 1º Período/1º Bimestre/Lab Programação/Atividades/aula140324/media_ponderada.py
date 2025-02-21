'''
Calcular a média de um aluno numa disciplina, sendo média=(provas + 3 x Trabalho + Participação/10)
provas = 3xprova1 + 3xprova2

média aritmética - soma todos os valores e divide pela quantidade de valores.
média harmônica - 
Média ponderada - --> peso - soma de peso x valor e divide pela soma dos pesos
média: 3.P + 3.P + 3.T + 1Partic/ 3+3+3+1

'''
print ("-"*80)
print ("Digite notas entre 0 e 10!")
print ("-"*80)

#entrada de dados

prova_1 = float(input("Digite a nota da prova 1: "))
prova_2 = float(input("Digite a nota da prova 2: "))
trabalho = float(input("Digite a nota do trabalho: "))
participacao = float(input("Digite a nota da participação: "))                

#processamento

provas = 3*prova_1 + 3*prova_2
media = (provas + 3*trabalho + participacao) / 10

#saída de dados

print (f"A média do aluno é {media}!!")