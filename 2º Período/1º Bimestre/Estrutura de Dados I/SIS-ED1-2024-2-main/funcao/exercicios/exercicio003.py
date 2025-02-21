def conta_vogais(texto):
    vogais = "aeiouAEIOU" #
    qtd = 0
    for letra in texto:
        # print(letra)
        if letra in vogais:
            qtd = qtd + 1
    return qtd

frase = "Ola Mundo"
quantidade = conta_vogais(frase)
print(f"{frase} tem {quantidade} vogais")