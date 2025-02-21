'''
Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve inofrmar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8.

Estado da memória: 0
opções:

(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar Memória
(6) Sair do programa

Qual opção você deseja?

'''



def menu ():
    print ("Escolha a opção desejada: ")
    print ("(1) Somar")
    print ("(2) Subtrair")
    print ("(3) Multiplicar")
    print ("(4) Dividir")
    print ("(5) Limpar Memória")
    print ("(6) Sair do programa")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def leitura (memoria = 0):
    print (f"O estado atual da memoria é {memoria}!")
    valor = float(input("Digite o segundo valor para realização do calculo escolhido: "))
    return valor


def soma (memoria, valor):
    return (memoria + valor)

'''def calculadora ():
    while comeco != 6:'''

        


comeco = menu()

operacao = soma()

