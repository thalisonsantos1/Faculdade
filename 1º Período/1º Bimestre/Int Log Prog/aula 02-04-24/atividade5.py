'''
Verifique se o triangulo é escaleno (todos os lados diferentes), isósceles (dois lados iguais) ou equilátero (todos os lados iguais)

'''

lado1 = int(input("Comprimento do lado 1 do triângulo: "))
lado2 = int(input("Comprimento do lado 2 do triângulo: "))
lado3 = int(input("Comprimento do lado 3 do triângulo: "))

if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print (f"O triangulo é escaleno!")
elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print (f"O triângulo é equilátero!!")
else:
    print (f"O triângulo é isósceles!!!")