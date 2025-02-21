#Em uma cozinha de restaurante existem apenas os ingredientes: tomate, agriao, bacon, pão de queijo, mel. Informe o total de combinações encontradas.

ingredientes = ["tomate", "agrião", "bacon", "pão de queijo", "mel"]
contador = 0

for i in ingredientes:
    for j in ingredientes:
        for k in ingredientes:
            if (i != j) and (j != k) and (i != k):
                print (f"{i} com {j} com {k}")
                contador += 1
print (f"Foram encontradas {contador} combinações")