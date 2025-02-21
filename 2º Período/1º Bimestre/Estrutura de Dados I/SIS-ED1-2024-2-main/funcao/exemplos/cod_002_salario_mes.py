
# funcao com parametros e sem retorno
def calcula_salario(horas_dia, dias_trabalhados, valor_hora = 88.5):
    # valor_hora = 88.5 # padrao - default
    salario = valor_hora*horas_dia*dias_trabalhados
    print(f"R$ {salario:.2f}")

if __name__ == "__main__":
    print("A1")
    calcula_salario(8, 18)
    print("A2")
    calcula_salario(3, 10, 100)
    print("A3")

