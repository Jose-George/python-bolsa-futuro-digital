
import time 

def gerar_lista():
    return [x for x in range(1_000_000)]

def test_performance(): 
    inicio = time.time()
    lista = gerar_lista()
    fim = time.time()
    duracao = fim - inicio
    print(f"Duração: {duracao} segundos")
    assert len(lista) == 1_000_000
    assert duracao < 2 