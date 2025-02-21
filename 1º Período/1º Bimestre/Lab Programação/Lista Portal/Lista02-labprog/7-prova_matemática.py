import random

acertos = 0
for i in range (5):
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)

    resultadoCorreto = (num_1 + num_2)

    print (f"Pergunta {i + 1}: Qual a soma de {num_1} + {num_2}?")
    resposta = int(input("Resposta: "))
    if resposta == resultadoCorreto:
        acertos += 1
        print ("Resposta correta!")
    else:
        print (f"Resposta incorreta. A resposta correta é {resultadoCorreto}.")
print (f"Você acertou {acertos} respostas em um total de 5 perguntas.")
