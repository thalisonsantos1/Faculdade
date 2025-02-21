lista = ['pizza', 'churrasco', 'sorvete', 'bacon', 'pipoca', 'alface', 'torresmo', 'ovo']
len (lista)

print (len(lista))

#imprimindo posição específica
print (lista [0])
print (lista [3])
#imprimindo o ultimo elemento da lista sem saber o número de elementos.
print (lista [len(lista)-1])

#imprimindo uma faixa de números (numeroinicial, limite da contagem+1, intervalo de contagem)
print (list(range(0,101,7)))

print (list(range(-50,301,13)))

#atribuindo a lista em uma variável
contagem = list(range(-123,124,2))
print (contagem)

#invertendo a ordem de uma lista
print (lista)
contrario = lista.reverse()
print (lista)

#contagem de caracteres em uma lista
y = list('Obabão? Tudo bão?')
print (y)

#exibindo a lista invertida ***não altera a variável***
print (y[::-1])

#1 - crie uma lista chamada nome com o seu nome inteiro
#2 - crie uma segunda variável que contenha o seu nome invertido
nome = list('Thalison de Oliveira Santos')
print (nome)
nomeinvertido = (nome[::-1])
print (nomeinvertido)
print (nome)

#criando uma lista vazia

A = []

#Adicionando um elemento no final da lista

A.append(12)
A.append('teste')
print (A)

A.insert(0,34) #insere o valor '34' na posição '0'
print (A)   

#removendo elemento da lista

Lista1 = ["teste", "abobrinha", "bolacha", "pizza"]
print (f"Lista1={Lista1}")
del Lista1[0] #apaga o primeiro elemento
print (f"Lista1={Lista1}")

print (50*"-")
escolhido=[Lista1.pop(0)] #escolhe determinado elemento na posição informada
print (f"Lista1={Lista1}")
print (f"Escolhido={escolhido}")

