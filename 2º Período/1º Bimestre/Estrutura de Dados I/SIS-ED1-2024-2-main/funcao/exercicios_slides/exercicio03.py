import os
from numerizer import numerize
from deep_translator import GoogleTranslator

def texto_para_digito(texto):
    # criamos o objeto pra traduzir  -> portuguese to english
    tradutor =  GoogleTranslator(source="pt", target="en")
    # funcao translate -> recebe um texto em pt e devolve o texto en
    traduzido = tradutor.translate(texto)
    # funcao numerize -> recebe um texto em en e devolve o digito
    numero = numerize(traduzido)
    return numero

def menu(mem):
    # os.system("cls")
    os.system("clear")
    print(f"Estado da memória: {mem}")
    print("Opções:")
    print()
    print("1- Somar")
    print("2- Subtrair")
    print("5- Limpar Memoria")
    print()
    return input("Qual opção você deseja? ")

def somar(x, y):
    return x+y

def calculadora():
    memoria = 0
    op = ""
    while op!= "6":
        op = menu(memoria)
        if op in ["1","2","3","4"]:
            valor = input("digite valor: ")
            if not valor.isdigit():
                valor = texto_para_digito(valor)

            valor_num = float(valor)
            if op == "1":
                memoria = somar(memoria, valor_num)
        elif op == "5":
            memoria = 0

calculadora()