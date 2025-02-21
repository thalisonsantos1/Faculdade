dia1 = "domingo"
dia2 = "segunda-feira"
dia3 = "terça-feira"
dia4 = "quarta-feira"
dia5 = "quinta-feira"
dia6 = "sexta-feira"
dia7 = "sábado"

numeroDia = int(input("Digite o número do dia da semana (1 - Dom até 7 - sábado): "))
while numeroDia not in ["1", "2", "3", "4", "5", "6", "7"]:
    print ("Dia invalido!")
    numeroDia = input("Digite o número do dia desejado: ")

if numeroDia in ["1", "2", "3", "4", "5", "6", "7"]:
    if numeroDia == "1":
        numeroDia = dia1
    elif numeroDia == "2":
        numeroDia = dia2
    elif numeroDia == "3":
        numeroDia = dia3
    elif numeroDia == "4":
        numeroDia = dia4
    elif numeroDia == "5":
        numeroDia = dia5
    elif numeroDia == "6":
        numeroDia = dia6
    elif numeroDia == "7":
        numeroDia = dia7
    
print (f"o dia escolhido foi {numeroDia}")