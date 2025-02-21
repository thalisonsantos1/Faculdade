def soma_digitos (n):  
    if n < 10:
        return n
    else:
        return n % 10 + soma_digitos (n // 10)
    

n = int(input("digite um número: "))

print (f"A soma dos dígitos do número {n} é {soma_digitos (n)}")
