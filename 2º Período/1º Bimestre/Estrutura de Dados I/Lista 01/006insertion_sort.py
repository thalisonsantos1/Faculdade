def insertion_sort(lista):
  for i in range (len(lista)):
    j = i
    while j >= 1 and lista[j][1] <= lista[j-1][1]:
      lista[j-1], lista [j] = lista[j], lista [j-1]
      j = j-1
    
  return lista


alunos = [("João", 90), ("José", 85), ("Marcos", 77), ("Maria", 65), ("Giovanna", 84), ("Bernardo", 74), ("Carlos", 74), ("Arlindo", 74)]
#alunos = [("João", 85), ("Ana", 90), ("Pedro", 78), ("Lucas", 95), ("Maria", 88)]
alunos_ordenados = insertion_sort(alunos)
#print(alunos_ordenados)

for aluno in alunos_ordenados:
  print (aluno)


  '''def insertion (lista):
    for i in range(1, len(lista)):
        j = i
        while j >= 1 and lista [j - 1] > lista[j]:
            lista [j - 1], lista [j] = lista [j], lista [j - 1]
            j = j - 1
    return lista'''