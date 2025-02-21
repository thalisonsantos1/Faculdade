def conta_letras (s, c):
    resultado =  s.count(c)
    if resultado >= 2:
        print (f"O caractere {c}, aparece {resultado} vezes.")
    else:
        print (f"O caractere {c}, aparece {resultado} vez.")

s = input("digite uma frase: ")
c = input("digite o caractere que deseja contar: ")    
conta_letras (s,c)