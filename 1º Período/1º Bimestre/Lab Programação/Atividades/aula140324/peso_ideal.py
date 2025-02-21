'''
Calcular o peso ideal de uma pessoa assumindo :
Homem: peso=(72,7 * altura)-58
Mulher: peso=(62,1*Altura)-44.7
'''
print ("=25")
print ("CALCULO DE PESO IDEAL")
print ("=25")

#entrada de dados:

altura = float(input("Digite a altura em metros do indivíduo: "))

#processamento de dados

peso_ideal_homem=(72.7*altura)-58
peso_ideal_mulher=(62.1*altura)-44.7

#saída

print(f"Peso ideal homens: {peso_ideal_homem:.3f}kg!")
print(f"Peso ideal mulheres: {peso_ideal_mulher}kg!")