faixa1 = 12000
faixa2 = 25000
comissao1 = 0.05
comissao2 = 0.10
comissao3 = 0.15
imposto2 = 0.15
imposto3 = 0.20
custof = float(input("Digite o custo fábrica do veículo: "))

if custof < faixa1:
    custo_cons = (custof * comissao1) + custof
    print (f"O custo ao consumidor do veículo é de R$ {custo_cons}")
elif custof >= faixa1 and custof < faixa2:
    custo_cons = (custof * comissao2) + (custof * imposto2) + custof
    print (f"O custo ao consumidor do veículo é de R$ {custo_cons}")
elif custof >= faixa2:
    custo_cons = (custof * comissao3) + (custof * imposto3) + custof
    print (f"O custo ao consumidor do veículo é de R$ {custo_cons}")