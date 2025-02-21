print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = input("Qual a opção desejada? ")
while opcao not in ["1", "2", "3", "4"]:
    print("Opção inválida.")
    opcao = input("Qual a opção desejada? ")
if opcao == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 + num2)
    print (f"O resultado da soma é {resultado}")
elif opcao == "2":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (max(num1, num2)) - (min(num1,num2))
    print (f"O resultado da diferença é {resultado}")
elif opcao == "3":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = (num1 * num2)
    print (f"O resultado da soma é {resultado}")
elif opcao == "4":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print ("Valor inválido")
        num2 = float(input("Digite o segundo número: "))
    else: 
        resultado = (num1 * num2)
        print (f"O resultado da soma é {resultado}")
