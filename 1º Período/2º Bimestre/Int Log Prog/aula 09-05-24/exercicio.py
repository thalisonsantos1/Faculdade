P = 20
Q = 8
R = "n"

if (P > Q and R == "n"):
    print ("Abobora")
else:
    print ("Teste")

'''
Fazendo a equivalencia
A ^ B
¬(¬(A ^ B)) dupla negação
¬(¬A v ¬B) de Morgan

A = P > Q
B = R == "n"
'''

P = 20
Q = 8
R = "n"

if not (not(P > Q) or not (R == "n")):
    print ("abobora")
else:
    print ("TESTE")