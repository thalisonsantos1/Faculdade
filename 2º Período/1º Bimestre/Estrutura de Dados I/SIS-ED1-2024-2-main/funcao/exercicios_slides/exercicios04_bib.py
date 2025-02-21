# importamos as bibliotecas
from numerizer import numerize
from deep_translator import GoogleTranslator

# criamos o objeto pra traduzir  -> portuguese to english
tradutor =  GoogleTranslator(source="pt", target="en")
texto = input("digite o texto: ")
# funcao translate -> recebe um texto em pt e devolve o texto en
traduzido = tradutor.translate(texto)
print(traduzido)
# funcao numerize -> recebe um texto em en e devolve o digito
numero = numerize(traduzido)
print(numero)