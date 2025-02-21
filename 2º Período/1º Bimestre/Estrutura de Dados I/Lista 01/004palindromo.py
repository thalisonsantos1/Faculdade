

def verifica_palindromo (frase):
    frase = frase.lower().replace (" ", "")
    invertido = frase[::-1]
    if frase == invertido:
        print ("A entrada é um palindromo!")
    else:
        print ("A entrada não é um palindromo!")

    
entrada = input("Digite uma palavra ou frase: ")
verifica_palindromo (entrada)

