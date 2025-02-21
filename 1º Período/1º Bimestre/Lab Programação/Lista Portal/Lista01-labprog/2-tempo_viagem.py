distancia_km = float(input("Digite a distância da viagem em quilômetros: "))
velocidade_media_kmh = float(input("Digite a velocidade média em km/h: "))
        
if distancia_km > 0 and velocidade_media_kmh > 0:
    tempo_de_viagem = (distancia_km / velocidade_media_kmh)
print(f"O tempo de viagem é de aproximadamente {tempo_de_viagem:.2f} horas")

