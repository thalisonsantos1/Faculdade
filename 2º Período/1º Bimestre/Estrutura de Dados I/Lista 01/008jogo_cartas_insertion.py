def insertion_sort(cartas):
  for i in range (1, len(cartas)):    
    j = i
    while j >= 0 and cartas [j-1] > cartas[j]:
      cartas[j-1], cartas[j] = cartas[j], cartas[j-1]
      j = j-1
    

mao = [2, 3, 10, 5, 7]
insertion_sort(mao)
print(mao)