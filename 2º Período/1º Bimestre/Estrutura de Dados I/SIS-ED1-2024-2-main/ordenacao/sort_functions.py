def selection_sort(L):
    for i in range(len(L)-1):
        menor = i
        for j in range(i+1,len(L)):
            if L[menor] > L[j]:
                menor = j
        L[i],L[menor] = L[menor], L[i]
        print(L)


# teste
if __name__ == "__main__":
    lista = [2,5,4,8,9,7]
    print(lista)
    selection_sort(lista)
    print(lista)