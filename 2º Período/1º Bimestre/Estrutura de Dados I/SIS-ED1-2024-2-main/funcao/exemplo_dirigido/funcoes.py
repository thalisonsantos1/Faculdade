# Gerador de senhas seguras
"""
Crie uma funcao chamada gerar_senha que receba 3 parametros opcionais:
-- tamanho (int) - Definir o comprimento da senha a ser gerada. O valor padrao deve ser 8.
-- incluir_numeros (bool) - Define se a senha deve incluir numeros (0-9). O valor padrao deve ser True
-- incluir_caracteres_especiais (bool) - Define se a senha deve incluir caracteres especiais (como @, #, $, ., etc.). O valor padrao deve ser True

Descricao: A funcao deve retornar uma string que represente a senha gerada, conforme as especificadas. 
Ex: se invocar:
gerar_senha(incluir_numeros=True,incluir_caracteres_especiais=False)---> devolver senha numerica com oito digitos

Requisitos:
1- A funcao nao deve gerar senhas com tamanho inferior a 4 (quatro). Caso contrario, retornar uma mensagem: 'O tamanho minimo para a senha e 4 caracteres'
2- Caso a senha nao tenha numeros nem caracteres especiais, ela vai ser composta apenas letras. Sempre deve ter letras.
"""
import random
import string

def gerar_senha(tamanho=8,numeros=True,especiais=True):
    if tamanho < 4:
        return "O tamanho minimo para a senha é 4 caracteres"
    senha = ""
    # for i in range(tamanho):
    i = 0
    while len(senha) < tamanho:
        senha = senha + gerar_letras()
        if numeros:
            senha = senha + gerar_numeros()
        if especiais:
            senha = senha + gerar_especiais()
   
    # senha = random.choices(senha, k = tamanho)
    # random.shuffle(senha) # embaralha
    return senha #"".join(senha)

def gerar_letras():
    letras = string.ascii_letters
    return random.choice(letras)

def gerar_numeros():
    numeros = string.digits
    return random.choice(numeros)

def gerar_especiais():
    especiais = string.punctuation
    return random.choice(especiais)

pwd = gerar_senha(tamanho=12,numeros=True, especiais=True)
print(pwd)