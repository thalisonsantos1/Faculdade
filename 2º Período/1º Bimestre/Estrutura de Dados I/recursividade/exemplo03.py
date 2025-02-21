def somaP (n, k):
    #caso base
    if n == 1:
        return k
    else: 
        return k**n + somaP(n-1, k)
 
if __name__ == "__main__":

    resultado = somaP (100, 55)
    print (resultado)
