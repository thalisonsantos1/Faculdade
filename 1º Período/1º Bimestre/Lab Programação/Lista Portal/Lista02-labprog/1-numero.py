import math

num = int(input("Digite um número inteiro maior que 0: "))

if num < 0:
        print ("Número inválido!")
        num = int(input("Digite um número inteiro maior que 0: "))
else:
    lognum = math.log (num)
    print (lognum)