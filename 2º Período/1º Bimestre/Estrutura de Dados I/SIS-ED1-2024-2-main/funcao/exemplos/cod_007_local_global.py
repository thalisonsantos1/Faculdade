
def altera_nome(nome):
    # variavel local
    # global nome
    nome = "Feioso"
    print("----dentro da funcao----")
    print(nome)

# variavel global
nome = "Lindovaldo"
altera_nome(nome)
print("----fora da funcao----")
print(nome)
    
