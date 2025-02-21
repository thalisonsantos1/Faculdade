'''
Fazer um programa que pergunte o mês do ano em número e informe o mês correspondente:

ex.: 
--> entrada: qual o mês desejado? 5

--> Saída: você escolheu o mês de maio

Caso o usuário digitar um mês invalido, escreva Mẽs incorreto
ex.: 
--> entrada: qual o mês desejado? 15

--> saída: mês incorreto.

'''

var1 = "Janeiro"
var2 = "Fevereiro"
var3 = "Março"
var4 = "Abril"
var5 = "Maio"
var6 = "Junho"
var7 = "Julho"
var8 = "Agosto"
var9 = "Setembro"
var10 = "Outubro"
var11 = "Novembro"
var12 = "Dezembro"

mes = input("Digite o número do mês desejado: ")

while mes not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" ]:
    print ("Mẽs invalido!")
    mes = input("Digite o número do mês desejado: ")

if mes in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12" ]:
    if mes == "1":
        mes = var1
    elif mes == "2":
        mes = var2
    elif mes == "3":
        mes = var3
    elif mes == "4":
        mes = var4
    elif mes == "5":
        mes = var5
    elif mes == "6":
        mes = var6
    elif mes == "7":
        mes = var7
    elif mes == "8":
        mes = var8
    elif mes == "9":
        mes = var9
    elif mes == "10":
        mes = var10
    elif mes == "11":
        mes = var11
    elif mes == "12":
        mes = var12
print (f"o mês escolhido foi o mês de {mes}")