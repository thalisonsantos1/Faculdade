class Calculadora:
    """Classe que implementa operações matemáticas básicas"""
    
    def soma(self, a, b):
        """Realiza a soma de dois valores"""
        if isinstance(a, list) and isinstance(b, list):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            return a + b
    
    def subtracao(self, a, b):
        """Realiza a subtração de dois números"""
        return a - b
    
    def multiplicacao(self, a, b):
        """Realiza a multiplicação de dois números"""
        return a * b
    
    def divisao(self, a, b):
        """Realiza a divisão de dois números"""
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b
