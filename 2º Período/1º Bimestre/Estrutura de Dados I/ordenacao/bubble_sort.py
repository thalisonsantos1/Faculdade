def bubble (lista):
    j = len(lista)-1
    while j > 0:
        for i in range (0, j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
            
        j = j - 1
    return lista

numeros = [97, 73, 14, 30, 81, 38, 65, 42, 74, 15, 79, 43, 51, 29, 80, 63, 55, 77, 61, 28, 70, 20, 11, 64, 54, 96, 53, 24, 67, 89, 95, 82, 90, 46, 44, 87, 32, 37, 12, 100, 16, 36, 99, 8, 59, 60, 75, 93, 35, 85]
bubble (numeros)
print (numeros)