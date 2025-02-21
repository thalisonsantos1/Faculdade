def quick_particao(lista, esq, dir):
    if len(lista) <= 1:
        return lista
    else:
        indice_pivo = (esq + dir) // 2
        pivo = lista[indice_pivo]
        i = esq
        j = dir
        while True:
            while lista[i] <= pivo and i < dir:
                i += 1

            while lista[j] >= pivo and j > esq:
                j -= 1
            
            if i >= j: # na posicao do pivo
                return i
            
            # troca de posicoes
            lista[i], lista[j] = lista[j], lista[i]

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        local_pivo = quick_particao(lista, inicio, fim)
        quick_sort(lista, inicio, local_pivo-1)
        quick_sort(lista, local_pivo+1, fim)

if __name__ == "__main__":
    vetor = [3,6,4,5,1,7,2]
    print(vetor)
    quick_sort(vetor, 0, 6)
    print(vetor)