vendas_mensais = float(input("Digite o total das vendas mensais: "))

faixa1 = 20000
faixa2 = 40000
faixa3 = 60000
faixa4 = 80000
faixa5 = 100000


if vendas_mensais < faixa1:
    comissao = (vendas_mensais * 0.14) + 400
    print (f"A comissão a ser paga é de R$ {comissao:.2f}")
elif vendas_mensais >= faixa1 and vendas_mensais < faixa2:
    comissao = (vendas_mensais * 0.14) + 500
    print (f"A comissão a ser paga é de R$ {comissao:.2f}")
elif vendas_mensais >= faixa2 and vendas_mensais < faixa3:
    comissao = (vendas_mensais * 0.14) + 550
    print (f"A comissão a ser paga é de R$ {comissao:.2f}")
elif vendas_mensais >= faixa3 and vendas_mensais < faixa4:
    comissao = (vendas_mensais * 0.14) + 600
    print (f"A comissão a ser paga é de R$ {comissao:.2f}")
elif vendas_mensais >= faixa4 and vendas_mensais < faixa5:
    comissao = (vendas_mensais * 0.14) + 650
    print (f"A comissão a ser paga é de R$ {comissao:.2f}")
elif vendas_mensais >= faixa5:
    comissao = (vendas_mensais * 0.16) + 700
    print (f"A comissão a ser paga é de R$ {comissao:.2f}")    