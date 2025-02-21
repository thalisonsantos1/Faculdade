op = input("Digite (S) para soma e (M) para multiplicar:")

while op not in ["S", "s", "M", "m" ]:
    print ("opção incorreta.")
    op = input("Digite (S) para somar ou (M) para multiplicar:" )

if op in ["S", "s", "M", "m" ]:
     x = int(input("Digite o primeiro valor: "))
     y = int(input("Digite o segundo valor: "))

if op == "S" or op == "s":
    r = (x+y)
    print (f"o resultado é {r}")
    
elif op == "M" or op == "m":
        r = (x*y)
        print (f"o resultado é {r}")