numero= int(input("Digite um número inteiro: "))
if numero > 0 or numero % 2 == 0: #numero divisível por 2 com resto 0. Se houver resto é falso.
    print (f"O número {numero} é positivo ou par!!")
else:
    print (f"O número {numero} não é positivo ou par")