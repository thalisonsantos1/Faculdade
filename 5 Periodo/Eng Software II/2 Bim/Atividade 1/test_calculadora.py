'''Testes unitários'''

from CALC.calculadora import Calculadora

def test_soma():
    """Testa o método soma isoladamente, com diferentes tipos de entradas"""

    #Arrange
    calc = Calculadora()
    a = 2
    b = 3
    #fim_arrange

    #ACT
    #Chamada da função a ser testada
    #Fim_ACT
    #inteiros positivos
    assert calc.soma(a, b) == 5

    #inteiros negativos
    assert calc.soma(-7, 4) == -3

    #floats
    assert calc.soma(1.2, 3.4) == 4.6   

    #strings
    assert calc.soma("1", "2") == "12"

    #listas
    assert calc.soma([1, 2], [3, 4]) == [1, 2, 3, 4]


def test_subtracao():
    """Testa o método subtração isoladamente, com diferentes tipos de entradas"""

    #Arrange
    calc = Calculadora()
    #fim_arrange

    #inteiros positivos
    assert calc.subtracao(10, 3) == 7

    #inteiros negativos
    assert calc.subtracao(-5, -2) == -3

    #floats
    assert calc.subtracao(10.5, 3.2) == 7.3


def test_multiplicacao():
    """Testa o método multiplicação isoladamente, com diferentes tipos de entradas"""

    #Arrange
    calc = Calculadora()
    #fim_arrange

    #inteiros positivos
    assert calc.multiplicacao(4, 5) == 20

    #inteiros negativos
    assert calc.multiplicacao(-3, 2) == -6

    #floats
    assert calc.multiplicacao(2.5, 4.0) == 10.0


def test_divisao():
    """Testa o método divisão isoladamente, com diferentes tipos de entradas"""

    #Arrange
    calc = Calculadora()
    #fim_arrange

    #inteiros positivos
    assert calc.divisao(10, 2) == 5

    #inteiros negativos
    assert calc.divisao(-8, 2) == -4

    #floats
    assert calc.divisao(7.5, 2.5) == 3.0


def test_varias_operacoes():
    """Testa uma cadeia de operações combinadas"""

    #Arrange
    calc = Calculadora()
    #fim_arrange

    #Teste de cadeia de operações: (10 + 5) - 3 * 2 / 2
    resultado1 = calc.soma(10, 5)  # 15
    assert resultado1 == 15

    resultado2 = calc.subtracao(resultado1, 3)  # 12
    assert resultado2 == 12

    resultado3 = calc.multiplicacao(resultado2, 2)  # 24
    assert resultado3 == 24

    resultado4 = calc.divisao(resultado3, 2)  # 12.0
    assert resultado4 == 12.0


def test_divisao_por_zero():
    """Testa se divisão por zero lança ValueError"""

    #Arrange
    calc = Calculadora()
    #fim_arrange

    #Testa se divisão por zero levanta ValueError
    try:
        calc.divisao(10, 0)
        assert False, "Deveria ter lançado ValueError"
    except ValueError:
        assert True

    