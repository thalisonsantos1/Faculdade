'''
Somar 3 números

    num1 --> 1º numero
    num2 --> 2º numero
    num3 --> 3º numero

    resultado --> num1 + num2 + num3

mostrar resultado
'''

for i in range(4):
    print(f"execução {i+1}")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    resultado = num1 + num2 + num3

    print(f"O resultado é {resultado}!!")