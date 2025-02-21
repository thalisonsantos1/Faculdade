comidas = ["bacon","lasanha","churrasco"]
frutas = ["pera","uva"]

print ("lista de comidas")
for lista1 in comidas:
    print (lista1)

print ("Lista de Frutas")
for lista2 in frutas:
    print (lista2)

print ()    
for lista1 in comidas:
    for lista2 in frutas:
        print (f"Itens: {lista1} e {lista2}")