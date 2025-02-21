def fatorial (n):
    if n > 0:
        #chamada recursiva
        return n*fatorial(n-1)
    else: #caso base
        return 1

if __name__ == "__main__":
    valor = 5
    resultado = fatorial(valor)
    print (f"{valor} != {resultado}")