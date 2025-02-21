#para entrega no portal 
#suponha que você tenha duas listas representando cores de camisas e calças disponíveis em uma loja de roupas. O objetivo é gerar todas as combinações possíveis de pares de cores, onde cada par consiste em uma cor de camisa e uma cor de calça. 
#As disponibilidades de cores são:
    #camisas: vermelho, azul, verde, amarelo e roxo;
    #calças: preto, cinza, branco, bege, marrom

camisas = ["vermelho", "azul", "verde", "amarelo", "roxo"]
calcas = ["preto", "cinza", "branco", "bege", "marrom"]
contador = 0

for x in camisas:
    for y in calcas:
        contador += 1
        print (f"Combinação {contador}: camisa {x} com calça {y}")
