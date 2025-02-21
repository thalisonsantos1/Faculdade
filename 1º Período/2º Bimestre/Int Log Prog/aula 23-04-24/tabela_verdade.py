total_linhas = 0
possibilidades = [True, False]

for A in possibilidades:
    for B in possibilidades:
        for C in possibilidades:
            if not (A and B) or C:
                resultado_formula = "True"
            else:
                resultado_formula = "False"
            print (f"A = {A} \t B = {B} \t C = {C} \t Formula = {resultado_formula}")
            total_linhas += 1
print (f"Total de linhas: {total_linhas}")