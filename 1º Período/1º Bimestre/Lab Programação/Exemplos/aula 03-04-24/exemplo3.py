valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))

maior_que = valor1 > valor2
igualdade = valor1 == valor2

if (valor1 > valor2) or (valor1 == valor2):
    print(f"{valor1} é maior ou igual a {valor2}")
else:
    print(f"{valor2} é maior que {valor1}")