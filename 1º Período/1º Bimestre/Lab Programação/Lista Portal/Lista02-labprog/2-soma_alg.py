numero = int(input("Digite um número inteiro maior que zero: "))

soma = 0
if numero < 0:
    print("Número inválido")
    numero = int(input("Digite um número inteiro maior que zero: "))
else: 
    while numero > 0:
        resto = numero % 10
        numero = (numero - resto)/10
        soma = soma + resto
print (f"A soma dos algarismos é {soma}")