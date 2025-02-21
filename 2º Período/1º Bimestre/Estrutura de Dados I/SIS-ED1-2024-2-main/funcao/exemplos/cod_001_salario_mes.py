
# def -> definir uma funcao
# def nome_da_funcao(<parametros>):

# funcao com parametros e sem retorno
def calcula_salario(horas_dia, dias_trabalhados):
    valor_hora = 88.5
    salario = valor_hora*horas_dia*dias_trabalhados
    print(f"R$ {salario:.2f}")

print("___________________________")
print(__name__)
if __name__ == "__main__":
    calcula_salario(8, 18)
    calcula_salario(3, 10)


#
# horas_dia = 8
# valor_hora = 88.5
# dias_trabalhados = 18

# salario = horas_dia*valor_hora*dias_trabalhados

# print(f"R$ {salario:.2f}")

# horas_dia = 3
# valor_hora = 88.5
# dias_trabalhados = 10

# salario = horas_dia*valor_hora*dias_trabalhados

# print(f"R$ {salario:.2f}")