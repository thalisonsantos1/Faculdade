impMG = 0.93
impSP = 0.88
impRJ = 0.85
impMS = 0.92

valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite o estado destino do produto (MG, SP, RJ, MS): ").upper()
while True:
    if estado_destino != "MG" and estado_destino != "SP" and estado_destino != "RJ" and estado_destino != "MS":
        print ("Estado inválido!")
        estado_destino = input("Digite o estado destino do produto (MG, SP, RJ, MS): ").upper()
        if estado_destino == "MG":
            valorFinal = (valor_produto / impMG)
            print (f"O valor do produto com desconto é R$ {valorFinal:.2f}")
        elif estado_destino == "SP":
            valorFinal = (valor_produto / impSP)
            print (f"O valor do produto com desconto é R$ {valorFinal:.2f}")
        elif estado_destino == "RJ":
            valorFinal = (valor_produto / impRJ)
            print (f"O valor do produto com desconto é R$ {valorFinal:.2f}")
        elif estado_destino == "MS":
            valorFinal = (valor_produto / impMS)
            print (f"O valor do produto com desconto é R$ {valorFinal:.2f}")
    else:
        break


