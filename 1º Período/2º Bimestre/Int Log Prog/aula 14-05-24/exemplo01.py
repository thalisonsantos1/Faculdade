#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Curso de Sistemas de Informação
Disciplina: introdução à lógica de programação
Prof. Dr. Dorival M. Machado Jr.
"""

possivel = [True, False]   

linhas=0
verdade=0
mentira=0
tabela1 = []

linhas2=0
verdade2=0
mentira2=0
tabela2 = []

print('Para o correto funcionamento, utilize a terminologia de variáveis: "a", "b" e "c" (minúsculas)')


formula=input('Digite a fórmula 1: ')
formula2=input('Digite a fórmula 2: ')

#------- geração da tabela verdade da fórmula 1--------------------
for a in possivel:
    for b in possivel:
        for c in possivel:
            if eval(formula):
                resultadoF=True
                verdade+=1  
            else:   
                resultadoF=False
                mentira+=1

            print(f'A = {a} \t B = {b} \t C = {c} \t H={resultadoF}')
            tabela1.append(resultadoF)
            linhas+=1

print(f'Total de linhas com resultado VERDADEIRO: {verdade}')
print(f'Total de linhas com resultado FALSO: {mentira}')
print(f'Total de linhas da tabela: {linhas}')

if (linhas == verdade):
    tipoFormula='TAUTOLÓGICA'
    
elif (linhas == mentira):
    tipoFormula='CONTRADITÓRIA'
    
else:
    tipoFormula='SATISFATÓRIA'

print(f'Esta fórmula é {tipoFormula}')


#------- geração da tabela verdade da fórmula 2--------------------
for a in possivel:
    for b in possivel:
        for c in possivel:
            if eval(formula2):
                resultadoF=True
                verdade2+=1  
            else:   
                resultadoF=False
                mentira2+=1

            print(f'A = {a} \t B = {b} \t C = {c} \t H={resultadoF}')
            tabela2.append(resultadoF)
            linhas2+=1

print(f'Total de linhas com resultado VERDADEIRO: {verdade2}')
print(f'Total de linhas com resultado FALSO: {mentira2}')
print(f'Total de linhas da tabela: {linhas2}')

if (linhas2 == verdade2):
    tipoFormula='TAUTOLÓGICA'
    
elif (linhas2 == mentira2):
    tipoFormula='CONTRADITÓRIA'
    
else:
    tipoFormula='SATISFATÓRIA'

print(f'Esta fórmula é {tipoFormula}')

#------- fazendo a comparação de resultado das fórmulas

print("FAZENDO ANÁLISE DE EQUIVALÊNCIA ENTRE AS FÓRMULAS:")
if tabela1 == tabela2:
    print("As fórmulas são equivalentes.")
else:
    print("As fórmulas não são equivalentes.")