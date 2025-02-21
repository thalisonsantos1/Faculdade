total_linhas = 0
possibilidades = [True, False]
total_true = 0
total_false = 0

for A in possibilidades:
    for B in possibilidades:
        if not (A and not (not B or A)):
            resultado_formula = "True"
            total_true += 1
        else:
            resultado_formula = "False"
            total_false += 1
        print (f"A = {A} \t B = {B} \t Formula = {resultado_formula}")
        total_linhas += 1
print (f"Total de linhas: {total_linhas}")

if total_false == 0:
    print ("Formula Tautológica")
elif total_true == 0:
    print ("Fórmula Contraditória")
else:
    print ("Fórmula Satisfatória")