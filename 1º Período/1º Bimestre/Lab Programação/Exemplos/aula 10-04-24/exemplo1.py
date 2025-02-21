numero = int(input("Digite um número inteiro: "))
resto = numero%2 #% calcula o resto da divisão
   
if resto == 0:
    print (f"{numero} é par!")
    if numero < 0:
        print (f"{numero} é negativo")
else:
    print (f"{numero} é ímpar!" )
    if numero < 0:
        print (f"{numero} é negativo")
    
    