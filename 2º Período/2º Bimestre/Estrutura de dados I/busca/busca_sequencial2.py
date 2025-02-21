vetor = ["quadrado", "circulo", "triangulo invertido", "triangulo", "estrela", "smile"]

def busca_sequencial2 (vetor, nome_procurado):
    for i in range(len(vetor)):
        if vetor [i] == nome_procurado:
            return i
    return -1

if __name__ == "__main__":
    print (busca_sequencial2 (vetor, "estrela"))
    resultado = "bola" in vetor
    print (resultado)