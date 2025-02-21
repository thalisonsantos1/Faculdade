# reuso de função já definida em outros arquivos

from cod_003_salarioMes import ler_horas_dia, calcula_salario # importando funções específicas
from cod_003_salarioMes import * # importando todas as funções do fonte especificado


h = ler_horas_dia ()
salario = calcula_salario (h, 15, 50)

print (f"R$ {salario:.2f}") 