compras = input("Vamos fazer uma lista de compras? (S-Sim N-Não)")
if compras.lower() == "s":
    lista = []
    contador = 0 #variável para contar a quantidade de itens na lista
    contador_1 = 1 #variável para indicar o item a ser digitado
    while True:
        item = input(f"Digite o item {contador_1} da lista ou '99' para sair: ")
        lista.append(item)# adiciona o item na lista
        contador_1 += 1
        contador += 1 #incrementando o contador
        #print (f"Sua lista tem {contador} itens, sendo eles: {lista}")
        if item == '99':
            break
    lista.remove("99")
    print(f"Sua lista tem {contador -1} itens sendo eles: {lista}")
        
else:
    print("Ok, finalizando agora")