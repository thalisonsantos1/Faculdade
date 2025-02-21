import math

xb = float(input("Digite o Xb: "))
xa = float(input("Digite o Xa: "))
yb = float(input("Digite o yb: "))
ya = float(input("Digite o ya: "))

x=((xb-xa)**2)
y=((yb-ya)**2)

raiz = math.sqrt(x+y)

print(f"A distancia é {raiz:.2f}.")