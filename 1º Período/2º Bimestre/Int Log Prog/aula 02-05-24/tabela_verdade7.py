'''
Aluno: Thalison de Oliveira Santos
R.A.: 003540

'''
total_linhas = 0
total_true = 0
total_false = 0
possibilidades = [True, False]
variaveis = int(input("Quantas variáveis a fórmula terá? (digite 2 ou 3 ou 0 para sair): "))


while variaveis != 2 and variaveis != 3 and variaveis != 0:
    variaveis = int(input("Quantas variáveis a fórmula terá? (digite 2 ou 3 ou 0 para sair): "))
    if variaveis == 0:
        break

if variaveis == 2:
    formula = input ("Digite a fórmula desejada: ")
    for A in possibilidades:
        for B in possibilidades:
            if eval (formula):
                resultado_formula = "True"
                total_true += 1
            else:
                resultado_formula = "False"
                total_false += 1
            print (f"A = {A} \t B = {B} \t  Formula = {resultado_formula}")
            total_linhas += 1
elif variaveis == 3:
    formula = input ("Digite a fórmula desejada: ")
    for A in possibilidades:
        for B in possibilidades:
            for C in possibilidades:
                if eval (formula):
                    resultado_formula = "True"
                    total_true += 1
                else:
                    resultado_formula = "False"
                    total_false += 1
                print (f"A = {A} \t B = {B} \t C = {C} \t  Formula = {resultado_formula}")
                total_linhas += 1

print (f"Total de True's: {total_true}")
print (f"Total de False's: {total_false}")
print (f"Total de linhas: {total_linhas}")

if total_false == 0:
    print ("Formula Tautológica")
elif total_true == 0:
    print ("Fórmula Contraditória")
else:
    print ("Fórmula Satisfatória")

    
