from exercicio_ import eh_par

def test_eh_par_com_numero_par():
    assert eh_par(4) == True

def test_eh_par_com_numero_impar():
    assert eh_par(5) == False

def test_eh_par_com_zero(): 
    assert eh_par(0) == True
