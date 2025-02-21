'''
verifique se uma pessoa pode votar:
-- idade maior ou igual a 16 anos.
-- idade menor ou igual a 70 anos.

'''

idade = int(input("Informe a idade do indivíduo: "))
if idade >= 16 and idade <= 70:
    print (f"O indivíduo está apto a votar!")
else:
    print (f"O indivíduo está impedido de votar!")
