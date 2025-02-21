def altera_nome ():
    #variável local
    nome = "Feioso"
    print ("---- dentro da função -----")
    print (nome)



#variável global
nome = "Thalison"
altera_nome ()
print ("----- Fora da função -----")
print  (nome)