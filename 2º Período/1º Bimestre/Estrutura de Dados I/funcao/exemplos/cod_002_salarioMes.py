#def --> definir função, seguida do nome da função e seguida dos parentesis, podendo ter parâmetros ou não


#função com parametros e sem retorno.
def calcula_salario (horas_dia, dias_trabalhados, valor_hora = 88.5):
    #valor_hora = 88.50 já informado nos parametros, caso o valor não seja inserido pelo usuário
    salario = horas_dia * valor_hora * dias_trabalhados
    print (f"R$ {salario:.2f}")    


if __name__ == "__main__":
    calcula_salario (8, 18)
    calcula_salario (3, 10, 100)












'''horas_dia = 8
valor_hora = 88.50
dias_trabalhados = 10

salario = horas_dia * valor_hora * dias_trabalhados

print (f"R$ {salario:.2f}")'''