# from cod_003_salario_mes import ler_horas_dia, calcula_salario
# * importa todas as funcoes de cod_003_salario_mes
from cod_003_salario_mes import *

h = ler_horas_dia()
salario = calcula_salario(h, 15, 50)

print(f"R$ {salario:.2f}")

