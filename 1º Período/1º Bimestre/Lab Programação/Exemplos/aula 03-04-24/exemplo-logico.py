valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

igualdade = valor1 == valor2
print (f"A afirmação que valor {valor1} é igual {valor2} é {igualdade}")

print(type(igualdade))

if igualdade:
    print ("SÃO IGUAIS!!")

if not igualdade: #negação da afirmação igualdade
    print ("SÃO DIFERENTES")

print ("FIM DO PROGRAMA!")