
def fatorial(numero):
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def test_fatorial(): 
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(5) == 120

def test_fatorial_falha(): 
    assert fatorial(5) != 119