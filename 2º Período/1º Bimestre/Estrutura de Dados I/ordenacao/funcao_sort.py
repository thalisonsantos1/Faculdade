def selection_sort (L):
    for i in range (0, len(L)-1):
        menor = i
        for j in range (i + 1, len (L)):
            if L [menor] > L [j]:
                menor = j
            L [i], L [menor], = L [menor], L [i]

    return [L]
if __name__=="__main__":
    lista = [1, 5, 6, 2, 3]
selection_sort (lista)
print (lista)

