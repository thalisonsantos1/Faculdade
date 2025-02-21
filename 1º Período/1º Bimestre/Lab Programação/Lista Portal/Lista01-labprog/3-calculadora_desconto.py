valor_original = float(input("Digite o valor original do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))/100
        
if valor_original >= 0 and 0 <= percentual_desconto <= 100:
    valor_com_desconto = (valor_original - (valor_original*percentual_desconto))
print(f"O valor com desconto é de R${valor_com_desconto:.2f}")
