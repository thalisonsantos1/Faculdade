numeros = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20,
    "trinta": 30,
    "quarenta": 40,
    "cinquenta": 50,
    "sessenta": 60,
    "setenta": 70,
    "oitenta": 80,
    "noventa": 90,
    "cem": 100,
    "cento": 100,
    "duzentos": 200,
    "trezentos": 300,
    "quatrocentos": 400,
    "quinhentos": 500,
    "seiscentos": 600,
    "setecentos": 700,
    "oitocentos": 800,
    "novecentos": 900,
    "mil": 1000
}

extenso = input("digite um numero por extenso: ")
extenso = extenso.replace(" e ", " ")
print(extenso)
partes = extenso.split(" ")
print(partes)

numero = 0
print("------parcial------")
ignora = False
for i in range(len(partes)):
    parte = partes[i]
    if not ignora:
        multiplicador = 1
        if i < len(partes)-1:
            if partes[i+1] == "mil":
                multiplicador = 1000
                ignora = True
            elif partes[i+1] == "milhoes" or partes[i+1]== "milhao":
                multiplicador = 1000000
                ignora = True
    
        valor = numeros[parte]
        valor = valor * multiplicador
        numero += valor
        print(numero)
    else:
        ignora = False
   
print('-----final-----')
print(numero)