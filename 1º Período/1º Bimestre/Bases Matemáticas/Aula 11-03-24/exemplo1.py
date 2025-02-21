# Definindo a função somar que retorna a soma de uma lista de valores
def somar(valores):
    return sum(valores)

# Definindo a função subtrair que retorna a subtração dos valores na ordem dada
def subtrair(valores):
    resultado = valores[0]
    for valor in valores[1:]:
        resultado -= valor
    return resultado

# Definindo a função multiplicar que retorna o produto dos valores
def multiplicar(valores):
    resultado = 1
    for valor in valores:
        resultado *= valor
    return resultado

# Definindo a função dividir que retorna o resultado da divisão dos valores na ordem dada
def dividir(valores):
    resultado = valores[0]
    for valor in valores[1:]:
        resultado /= valor
    return resultado

# Função principal para realizar a operação escolhida pelo usuário
def realizar_operacao():
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite o número correspondente à operação desejada: ")

    # Verifica se a escolha é válida
    if escolha not in ['1', '2', '3', '4']:
        print("Escolha inválida. Por favor, digite um número de 1 a 4.")
        return

    # Solicita o número de valores para a operação
    num_valores = int(input("Digite o número de valores para a operação: "))
    
    valores = []
    # Solicita os valores e adiciona à lista
    for i in range(num_valores):
        valor = float(input(f"Digite o {i+1}º valor: "))
        valores.append(valor)

    # Executa a operação escolhida com os valores fornecidos
    if escolha == '1':
        resultado = somar(valores)
        print(f"Resultado da soma: {resultado}")
    elif escolha == '2':
        resultado = subtrair(valores)
        print(f"Resultado da subtração: {resultado}")
    elif escolha == '3':
        resultado = multiplicar(valores)
        print(f"Resultado da multiplicação: {resultado}")
    elif escolha == '4':
        resultado = dividir(valores)
        print(f"Resultado da divisão: {resultado}")

# Executa a função principal se o script for executado diretamente
if __name__ == "_main_":
    realizar_operacao()