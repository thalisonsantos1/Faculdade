from numerizer import numerize
from deep_translator import GoogleTranslator


texto = "dois mil trezentos e cinquenta e sete"

tradutor = GoogleTranslator(source="pt", target="en")
traduzido = tradutor.translate(texto)

numerizado = numerize(traduzido)
numero = float(numerizado)

print (traduzido)
print (numero)
print (type(numero))


