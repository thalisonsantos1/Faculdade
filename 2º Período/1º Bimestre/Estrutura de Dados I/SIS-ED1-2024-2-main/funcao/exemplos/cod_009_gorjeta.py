def calcula_gorjeta(valor, percentual = 10):
    print(f"valor {valor}")
    print(f"percentual {percentual}")
    return valor*(percentual/100)

gorjeta = calcula_gorjeta(400)
print(gorjeta)
gorjeta = calcula_gorjeta(400, 5)
print(gorjeta)

