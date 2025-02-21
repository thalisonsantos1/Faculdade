def intercala (inicio, meio, fim, lista):
    i = inicio
    j = meio
    lista_ordenada = []
    while i < meio and j < fim:
        if lista[i] < lista[j]:
            lista_ordenada.append (lista[i])
            i += 1
        else:
            lista_ordenada.append (lista[j])
            j += 1
    
    # pq i == meio ou j == fim?
    # garantindo que vou pegar todos os elementos da primeira metade
    while i < meio:
        lista_ordenada.append (lista[i])
        i += 1

    # garantindo que vou pegar todos os elementos da segunda metade
    while j < fim:
        lista_ordenada.append (lista[j])
        j += 1
    
    #havia faltado esse for
    for m in range (inicio, fim):
        lista[m] = lista_ordenada[m - inicio]

    return lista_ordenada


def mergeSort(inicio, fim, lista):
    if inicio < fim - 1:
        meio = (inicio + fim) // 2
        mergeSort (inicio, meio, lista)
        mergeSort (meio, fim, lista)
        intercala (inicio, meio, fim, lista)

#main - principal
if __name__ == '__main__':

    valores = [29, 10, 14, 37, 13]
    mergeSort (0, len(valores), valores)
    print (valores)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''mergeSort ()
    inicio = 0
    fim = len(valores)
    meio = (inicio + fim) // 2
    intercala (inicio, meio, fim, valores)
    print (valores)'''