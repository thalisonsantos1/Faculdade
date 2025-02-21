from numerizer import numerize
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator (source="pt", target="en")
texto = input("Digite o texto: ")
traduzido = tradutor.translate(texto)
print (traduzido)