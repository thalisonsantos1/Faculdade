def cadastra_produtos():
    lista_produtos = []
    inserir = "s"
    while inserir.lower() == "s":
        item = {}
        item ["nome"] = input("Digite o nome do produto: ")
        item ["preco"] = input("Digite o preco do produto: ")
        item ["quantidade"] = input("Digite o quantidade do produto: ")
        lista_produtos.append (item)
        inserir = input("Deseja inserir mais um produto? [S/N]")
    print (lista_produtos)
    for produto in lista_produtos:
        print(produto["nome"])
        print(produto["preco"])
        print(produto["quantidade"])
        print("------")
    return lista_produtos

def selection_sort (produtos):
  for i in range (len(produtos)):
    min = i
    for j in range (i+1, len(produtos)):
      if produtos[min]["preco"] > produtos[j]["preco"]:
        min = j
    produtos[i], produtos[min] = produtos[min], produtos[i]
  print (produtos)

cadastra_produtos()
produtos_ordenados = selection_sort ()
