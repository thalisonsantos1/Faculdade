'''
Verifique se uma pessoa pode aposentar, se:
-- pelo menos 65 anos de idade e,
-- 30 anos ou mais de contribuição previdenciária.
'''

idade = float(input("Informe a idade em anos completos: "))
contribuicao = float(input("Informe o tempo de contribuição em anos: "))

if idade >= 65 and contribuicao >= 30:
    print (f"O indivíduo pode se aposentar!")
else:
    print (f"O indivíduo ainda não pode se aposentar!")