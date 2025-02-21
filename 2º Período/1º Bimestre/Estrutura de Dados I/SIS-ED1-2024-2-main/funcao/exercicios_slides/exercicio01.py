def fat(num):
    if num == 0:
        return 1
    else:
        resultado = 1
        for i in range(1,num+1):
            resultado *= i
        return resultado

def combinacao(N, M):
    possibilidades = fat(N)/(fat(M)*fat(N-M))
    print(possibilidades)
    return possibilidades

combinacao(8, 2)
