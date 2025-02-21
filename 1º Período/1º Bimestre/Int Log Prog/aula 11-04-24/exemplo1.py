# EX.1 Faça a contagem de combinações desta lisa
comidas = ['bacon','lasanha','churrasco','ervilha','mingau','hamburguer']
frutas = ['pera','uva','maça','melancia','goiaba']
contador = 0


print("VAMOS VER AS COMBINAÇÕES:")
for x in comidas:
    for y in frutas:
        print(f"{x} com {y}")
        contador += 1 #contando quantas combinações foram formadas

print (f"Foram um total de {contador} combinações!")