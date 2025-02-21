def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 24.9:
        return 'Peso normal'
    elif imc >= 25 and imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

def coletar_dados_paciente():
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    peso = float(input("Digite o peso do paciente (kg): "))
    altura = float(input("Digite a altura do paciente (m): "))
    return {
        'nome': nome,
        'telefone': telefone,
        'peso': peso,
        'altura': altura
    }

def main():
    dados_paciente = coletar_dados_paciente()
    imc = calcular_imc(dados_paciente['peso'], dados_paciente['altura'])
    classificacao = classificar_imc(imc)
    print(f"O IMC do paciente {dados_paciente['nome']} é {imc:.2f}")
    print(f"Classificação: {classificacao}")