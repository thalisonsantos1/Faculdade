total_linhas = 0
total_true = 0
total_false = 0
possibilidades = [True, False]

for A in possibilidades:
    for B in possibilidades:
        for C in possibilidades:
            for D in possibilidades:
                if ((not A or B) == (not (B and C))) == (D and (not C or B)):
                    resultado_formula = "True"
                    total_true += 1
                else:
                    resultado_formula = "False"
                    total_false += 1
                print (f"A = {A} \t B = {B} \t C = {C} \t C = {D} \t Formula = {resultado_formula}")
                total_linhas += 1
                
print (f"Total de True's: {total_true}")
print (f"Total de False's: {total_false}")
print (f"Total de linhas: {total_linhas}")

