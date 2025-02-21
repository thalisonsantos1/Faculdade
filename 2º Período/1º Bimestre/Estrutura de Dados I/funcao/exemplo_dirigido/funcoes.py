#gerador de senhas seguras

'''
Crie uma função chamada gerar_senha que receba 3 parametros opcionais:
- tamanho (int) - Definir o comprimento da senha a ser gerada. O valor padrão deve ser 8.
- incluir_numeros (bool) - Define se a senha deve incluir números (0-9). O valor  padrão deve ser True
- incluir_caracteres_especiais (bool) - Define se a senha deve incluir caracteres especiais como ( @, #, $ e etc). O valor padrão deve ser True

Descrição: a função deve retornar uma string que represente a senha gerada, conforme as especificações fornecidas.

ex: se invocar gerar_senha (incluir_numeros=True, incluir_caracteres_especiais=False) --> devolver uma senha numérica com oito dígitos.

Requisitos:
1 - A função não deve gerar senhas com tamanho inferior a 4 (quatro). Caso contrário, retornar mensagem de erro
2 - Caso a senha não tenha números nem caracteres especiais, ela será composta apenas de letras. Sempre deve ter letras.

''' 

import random
import string


def gerar_senha (tamanho = 8, numeros = True, especiais = True):
    if tamanho < 4:
        return "O tamanho mínimo par a senha é de 04 caracteres"
    senha = ""
    for i in range (tamanho):
        senha = senha + gerar_letras() 
        if numeros:
            senha = senha + gerar_numeros()
        if especiais:
            senha = senha + gerar_especiais()
    print (senha)
    senha = random.choices (senha, k = tamanho)
    random.shuffle (senha) #embaralha
    return "".join (senha)
    return senha


def gerar_letras():
    letras = string.ascii_letters
    return random.choice (letras)

def gerar_numeros():
    numeros = string.digits
    return random.choice (numeros)

def gerar_especiais():
    especiais = string.punctuation
    return random.choice (especiais)


pwd = gerar_senha (numeros=True, especiais=True)
print (pwd)




