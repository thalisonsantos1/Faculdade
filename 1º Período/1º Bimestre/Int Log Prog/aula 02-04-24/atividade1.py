'''
if CONDIÇÃO:
se
    faça isto

    ELSE:
senão       faça esse outro 
'''

#ex1: Verifique se um número digitado é positivo.

numero= int(input("Digite um número inteiro: "))
if numero > 0 and numero % 2 == 0: #numero divisível por 2 com resto 0. Se houver resto é falso.
    print (f"O número {numero} é positivo e par!!")
else:
    print (f"O número {numero} não é positivo")








