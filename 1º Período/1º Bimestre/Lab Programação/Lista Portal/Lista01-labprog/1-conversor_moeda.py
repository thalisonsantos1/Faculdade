'''def converter_para_dolar(valor_em_reais, taxa_dolar):
    return valor_em_reais / taxa_dolar

def main():
    try:'''
valor_em_reais = float(input("Digite o valor em reais: "))
taxa_dolar = float(input("Digite a taxa de câmbio do dólar (quantos reais valem 1 dólar): "))
        
valor_em_dolar = (valor_em_reais * taxa_dolar)
print(f"R${valor_em_reais:.2f} equivalem a US${valor_em_dolar:.2f}")
