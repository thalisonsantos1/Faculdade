#Conversão de moeda - real para dólar:

real = float(input("Insira o valor em reais: "))
dolar = float(input("Insira o valor em dólar: "))
valor_dolar = (real/dolar)

print (f"Na cotação atual, R$ {real} corresponde a U$$ {valor_dolar:.3}!!")