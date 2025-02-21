#def --> definir função, seguida do nome da função e seguida dos parentesis, podendo ter parâmetros ou não


#função com parametros e COM retorno.
def calcula_salario (horas_dia, dias_trabalhados, valor_hora = 88.5):
    #valor_hora = 88.50 já informado nos parametros, caso o valor não seja inserido pelo usuário
    salario = horas_dia * valor_hora * dias_trabalhados
    return salario #nesse momento, se o programa não usar o resultado em nenhum lugar ele é perdido

# função sem parametro e sem retorno

def boas_vindas ():
    print ("-"*10)
    print ("-"*5, "inicio","-"*5)

#função sem parametro e com retorno
def ler_horas_dia ():
    hd = float(input("Digite a quantidade de horas trabalhadas por dia: "))
    return hd

if __name__ == "__main__":
    boas_vindas ()
    horas = ler_horas_dia ()
    a = calcula_salario (horas, 18)
    horas = ler_horas_dia ()
    b = calcula_salario (horas, 10, 100)

    print (a)
    print (b)
    print (b*2)












'''horas_dia = 8
valor_hora = 88.50
dias_trabalhados = 10

salario = horas_dia * valor_hora * dias_trabalhados

print (f"R$ {salario:.2f}")'''