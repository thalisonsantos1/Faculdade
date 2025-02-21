# Tempo de viagem


distancia = float(input("Digite o valor em km: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))

tempo = (distancia/velocidade_media)
horas = int (tempo)
minutos = (tempo - horas)*60
print (f"o tempo de viagem é {horas} hora e {minutos:.f0}")