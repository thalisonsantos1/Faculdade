import random

mao = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#while = enquanto

while len(mao) > 0:
    sorteia = random.randint(0, len(mao)-1)
    print (mao[sorteia])
    del mao[sorteia]
    print(mao)
    input ("... continua")