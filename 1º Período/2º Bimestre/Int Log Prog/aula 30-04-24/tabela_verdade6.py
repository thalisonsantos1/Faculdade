'''
Existem 3 tipos de fórmulas:
1 - tudo verdadeiro: Tautológica, não serve pra nada.
2 - tudo falso: Contraditória, também não serve pra nada
3 - verdadeiro e falso: satisfatória

a - satisfatória - t:3 f:1 ok
b - satisfatória - t:2 f:2 ok
c - tautológica -  t:4 f:0 ok
d - satisfatória - t:2 f:2 ok
e - satisfatória - t:2 f:2 ok

'''

total_linhas = 0
total_true = 0
total_false = 0
possibilidades = [True, False]
formula = input ("Digite a fórmula (utilize a nomenclatura 'a' e 'b' para variáveis): ")

for A in possibilidades:
    for B in possibilidades:
        #for C in possibilidades:
            #for D in possibilidades:
                if eval (formula):
                    resultado_formula = "True"
                    total_true += 1
                else:
                    resultado_formula = "False"
                    total_false += 1
                print (f"A = {A} \t B = {B} \t  Formula = {resultado_formula}")
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

