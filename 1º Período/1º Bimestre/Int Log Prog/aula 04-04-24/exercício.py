nome = input("Informe seu nome: ")
num_1 = int(input("Digite o primeiro número inteiro: "))
num_2 = int(input("Digite o segundo número inteiro: "))

if num_1 == 99 and num_2 == 99: 
    print (f"{nome}, que números interessantes você escolheu!!")

if num_2 > num_1:
    print (f"{nome}, {num_2} é maior que {num_1}!")
if num_2 == num_1:
    print (f"{nome}, não existe um número maior que o outro!")
if num_2 < num_1:
    print (f"{nome}, {num_2} não é maior que {num_1}!")

pergunta = input("Quer fazer uma contagem até 10, de 2 em 2?? (S-Sim N-Não)")
#print (pergunta)

if pergunta.lower() == "s":
    for i in range (0,11,2):
        print (i)
elif pergunta.lower() != "s":
    print (f"Ok, {nome}, vamos prosseguir!")        

compras = input("Vamos fazer uma lista de compras? (S-Sim N-Não)")

if compras.lower() == "n":
    print(f"Ok, {nome}, finalizando agora!")
elif compras.lower() != "n":
    lista = []
    x = input("Digite o nome do item: "),
    lista.append(x) 
    print (lista)
    while x != "sair":
        x = input("Digite o nome do item: ")
        lista.append(x)
        print (lista)
    else:
        lista.remove ("99")
        print (f"Lista finalizada: {lista}")

#método do professor:
'''if compras.lower() == "s":
    lista = []
    while True:
        item = input("Digite o item da lista ou '99' para sair")
        if item == '99':
            break
        lista.append(item)
        print (f"Lista de compras: {lista}")
else:
    print("Ok, finalizando agora")'''
#*****************************************************************************


