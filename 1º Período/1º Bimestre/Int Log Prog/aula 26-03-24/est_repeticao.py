#Estruturas de repetição
#mecanismos para aproveitar o código

#estrutura FOR
print ("Número = 1")
print ("Número = 2")
print ("Número = 3")
print ("Número = 4")
print ("Número = 5")
print ("Número = 6")
print ("Número = 7")
print ("Número = 8")
print ("Número = 9")
print ("Número = 10")


for i in range (0,21):
    print(f"Este é o número {i}!!")


bebidas = ["cerveja","vinho","refrigerante","champagne","vodka","rum","água","whisky"]
for i in bebidas:
    print(f"A bebida escolhida é {i}!!")

for i in "1","2",8,2+2,"abobrinha":
    print (i)

#for i in range (0,1000001):
#    print (f"Número {i}!")


#Estrutura WHILE
    
x = 0
while x <= 10: #repetirá enquanto a condição não for atendida
    x = int (input("Digite um valor: "))

senha = "123456"
n = ""
while n != senha: #enquanto a senha não for correta, haverá repetição
    print ("Sistema Tabajara Plus Protection")
    n = input("Digite a senha: ")

nota = float(input("Digite a nota (0-100): "))
while nota < 0 or nota > 100:
    nota=float(input("Nota inválida. Tente novamente"))    
    #print (f"Nota inválida: {nota}. Tente novamente!") #código errado - causou looping
    print (f"A nota válida foi {nota}")

while True:
    n = int(input("Digite um número inteiro: "))
    print(f"Você digitou {n}")
    if n == 9:
        print ("Parabéns, agora podemos sair do loop")
        break