def bubble_sort(lista):
  s = len(lista)
  for i in range(s):
    for j in range(0, s-i-1):
      
      if len(lista[j]) > len(lista[j+1]):
        lista[j], lista[j+1] = lista[j+1], lista[j]

  return lista
  
frutas = ["maçã", "banana", "uva", "laranja", "abacaxi", "melão", "melancia", "castanha do pará"]
frutas_ordenadas = bubble_sort(frutas)
print(frutas_ordenadas)