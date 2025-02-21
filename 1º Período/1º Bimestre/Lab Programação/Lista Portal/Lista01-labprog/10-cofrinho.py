moeda1c = 0.01
moeda5c = 0.05
moeda25c = 0.25
moeda50c = 0.50
moeda1r = 1.00

qtdmoeda1c = int(input("Digite o número de moedas de R$ 0.01: "))
qtdmoeda5c = int(input("Digite o número de moedas de R$ 0.05: "))
qtdmoeda25c = int(input("Digite o número de moedas de R$ 0.25: "))
qtdmoeda50c = int(input("Digite o número de moedas de R$ 0.50: "))
qtdmoeda1r = int(input("Digite o número de moedas de R$ 1.00: "))

totalmoedas1c = (qtdmoeda1c * moeda1c)
totalmoedas5c = (qtdmoeda5c * moeda5c)
totalmoedas25c = (qtdmoeda25c * moeda25c)
totalmoedas50c = (qtdmoeda50c * moeda50c)
totalmoedas1r = (qtdmoeda1r * moeda1r)

totaleconomizado = (totalmoedas1c + totalmoedas5c + totalmoedas25c + totalmoedas50c + totalmoedas1r)

print(f"Há um total de R$ {totalmoedas1c:.2f} em moedas de 1 centavo!")
print(f"Há um total de R$ {totalmoedas5c:.2f} em moedas de 5 centavos!")
print(f"Há um total de R$ {totalmoedas25c:.2f} em moedas de 25 centavos!")
print(f"Há um total de R$ {totalmoedas50c:.2f} em moedas de 50 centavos!")
print(f"Há um total de R$ {totalmoedas1r:.2f} em moedas de 1 real!")
print(f"Parabéns! Você economizou R$ {totaleconomizado:.2f}!")