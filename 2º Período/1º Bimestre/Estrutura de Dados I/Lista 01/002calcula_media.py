def calculaMedia ():
    listaNotas = []
    for notas in range(0,10):
        notas = float(input("Digite as notas desejadas. Digite 99 para calcular a média. "))
        listaNotas.append (notas)
        #print (listaNotas)
        if notas == 99:
            del(listaNotas[-1])
            print (listaNotas)
            media = sum(listaNotas)/len(listaNotas)
            print (f"A média do aluno é {media:.2f}")
            break
        

calculaMedia ()