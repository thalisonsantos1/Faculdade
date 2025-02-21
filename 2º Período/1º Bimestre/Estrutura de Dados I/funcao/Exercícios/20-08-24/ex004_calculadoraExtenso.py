from numerizer import numerize
from deep_translator import GoogleTranslator


def menu (mem):
    print (f"Estado da memoria: {mem}")
    print ("Escolha a opção desejada: ")
    print ("(1) Somar")
    print ("(2) Subtrair")
    print ("(3) Multiplicar")
    print ("(4) Dividir")
    print ("(5) Limpar Memória")
    print ("(6) Sair do programa")
    return int(input("Digite a opção desejada: "))

def somar (x, y):
    return x + y

def subtrair (x, y):
    return x - y

def multiplicar (x , y):
    return x * y

def dividir (x, y):
    return x / y

def calculadora ():
    memoria = 0
    op = 0     
    while op != 6:
        op = menu (memoria)
        if op in [1, 2, 3, 4]:
            valor = input("Digite o valor em extenso para a operação: ")
            tradutor = GoogleTranslator(source="pt", target="en")
            traduzido = tradutor.translate(valor)
            numerizado = numerize(traduzido)
            numero = float(numerizado)
            
            if op == 1:
                memoria = somar (memoria, numero)
            elif op == 2:
                memoria = subtrair (memoria, numero)
            elif op == 3:
                memoria = multiplicar (memoria, numero)
            elif op == 4:
                memoria = dividir (memoria, numero)
        elif op == 5:
            memoria = 0
            print ("Memória limpa!")
        else: 
            print ("Opção inválida.")
    else:
        print ("ok. Encerarndo o programa!")
            

calculadora ()