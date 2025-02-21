
# funcao com parametros e COM retorno
def calcula_salario(horas_dia, dias_trabalhados, valor_hora = 88.5):
    # valor_hora = 88.5 # padrao - default
    salario = valor_hora*horas_dia*dias_trabalhados
    return salario

# funcao sem parametro e sem retorno
def boas_vindas():
    print("------------------------")
    print("---------inicio---------")

def ler_horas_dia():
    hd = float(input("Digite a qtd de horas trabalhadas por dia: "))
    return hd

if __name__ == "__main__":
    boas_vindas()

    print("A1")
    horas = ler_horas_dia()
    a = calcula_salario(horas, 18)
    print("A2")
    # b = calcula_salario(ler_horas_dia(), 10, 100)
    horas = ler_horas_dia()
    b = calcula_salario(horas, 10, 100)
    
    print("A3")

    print(f"a {a}")
    print(f"b {b}")
    print(f"o dobro de b = {b*2}")

