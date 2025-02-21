camisetasP = 10
camisetasM = 12
camisetasG = 15

pvendas = int(input("Digite quantas camisetas P foram vendidas: "))
mvendas = int(input("Digite quantas camisetas M foram vendidas: "))
gvendas = int(input("Digite quantas camisetas G foram vendidas: "))

totalP = (pvendas * camisetasP)
totalM = (mvendas * camisetasM)
totalG = (gvendas * camisetasG)
totalGeral = (totalP + totalM + totalG)

print ("Totais do pedido:")
print (f" Camisetas P: R${totalP},00:")
print (f" Camisetas M: R${totalM},00:")
print (f" Camisetas G: R${totalG},00:")
print (f"O total do pedido é de R$ {totalGeral},00!")