def selection_sort(L):
    for i in range(len(L)-1):
        menor = i
        for j in range(i+1,len(L)):
            if L[menor] > L[j]:
                menor = j
        L[i],L[menor] = L[menor], L[i]
        print(L)

def bubble_sort(L):
    print("-----")
    j = len(L)-1
    while j > 0:
        for i in range(0,j):
            if L[i] > L[i+1]:
                L[i],L[i+1] = L[i+1], L[i]
            print(L)
        j = j-1
    print("-----")

def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while j >= 1 and L[j-1] > L[j]:
            # trocar
            L[j-1], L[j] = L[j], L[j-1]
            j = j - 1
            print(L)

# teste
if __name__ == "__main__":
    lista = ["O", "R", "D", "E", "N", "A"]
    print(lista)
    selection_sort(lista)
    print(lista)