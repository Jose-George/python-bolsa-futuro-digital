# 🐍 Aula Prática: Testes Automatizados com Pytest

## 📌 Estrutura da Aula

1. Motivação: por que testar?
2. Instalação do Pytest
3. Primeiro teste (exemplo simples)
4. Testando funções utilitárias (strings e listas)
5. Testando classes e objetos
6. Uso de fixtures
7. Testes parametrizados
8. Testando exceções
9. Plugins e relatórios
10. Exercícios práticos

---

## 1️⃣ Motivação: Por que testar?

* Previne erros em produção
* Facilita refatoração
* Dá confiança ao evoluir o código
* Serve como **documentação viva** do sistema

---

## 2️⃣ Instalação do Pytest

```bash
pip install pytest
pytest --version
```

---

## 3️⃣ Primeiro Teste

### Arquivo `util.py`

```python
def inverter_string(texto: str) -> str:
    return texto[::-1]
```

### Arquivo `test_util.py`

```python
from util import inverter_string

def test_inverter_string():
    assert inverter_string("python") == "nohtyp"
    assert inverter_string("abc") == "cba"
```

➡️ Rodar com:

```bash
pytest
```

---

## 4️⃣ Testando Funções Utilitárias

### Arquivo `listas.py`

```python
def maior_elemento(lista):
    return max(lista)

def conta_ocorrencias(lista, elemento):
    return lista.count(elemento)
```

### Arquivo `test_listas.py`

```python
from listas import maior_elemento, conta_ocorrencias

def test_maior_elemento():
    assert maior_elemento([1, 5, 3]) == 5
    assert maior_elemento([-10, -3, -7]) == -3

def test_conta_ocorrencias():
    lista = ["maçã", "banana", "maçã", "uva"]
    assert conta_ocorrencias(lista, "maçã") == 2
    assert conta_ocorrencias(lista, "banana") == 1
    assert conta_ocorrencias(lista, "laranja") == 0
```

---

## 5️⃣ Testando Classes e Objetos

### Arquivo `carro.py`

```python
class Carro:
    def __init__(self, modelo, tanque=0):
        self.modelo = modelo
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros

    def dirigir(self, distancia):
        if distancia > self.tanque:
            raise ValueError("Combustível insuficiente")
        self.tanque -= distancia
```

### Arquivo `test_carro.py`

```python
import pytest
from carro import Carro

def test_abastecer():
    c = Carro("Fusca")
    c.abastecer(50)
    assert c.tanque == 50

def test_dirigir_sucesso():
    c = Carro("Uno", tanque=100)
    c.dirigir(30)
    assert c.tanque == 70

def test_dirigir_sem_combustivel():
    c = Carro("Gol", tanque=10)
    with pytest.raises(ValueError):
        c.dirigir(50)
```

---

## 6️⃣ Uso de Fixtures

Fixtures ajudam a **reaproveitar código de setup**.

```python
import pytest
from carro import Carro

@pytest.fixture
def carro_pronto():
    return Carro("Civic", tanque=50)

def test_civic_abastecido(carro_pronto):
    assert carro_pronto.tanque == 50
    assert carro_pronto.modelo == "Civic"
```

---

## 7️⃣ Testes Parametrizados

```python
import pytest
from util import inverter_string

@pytest.mark.parametrize("entrada,esperado", [
    ("python", "nohtyp"),
    ("123", "321"),
    ("radar", "radar"),  # palíndromo
])
def test_inverter_string_parametrizado(entrada, esperado):
    assert inverter_string(entrada) == esperado
```

---

## 8️⃣ Testando Exceções

```python
import pytest
from listas import maior_elemento

def test_lista_vazia_erro():
    with pytest.raises(ValueError):  # max([]) gera ValueError
        maior_elemento([])
```

---

## 9️⃣ Plugins e Relatórios

* **Cobertura de código:**

```bash
pip install pytest-cov
pytest --cov=.
```

* **Execução paralela:**

```bash
pip install pytest-xdist
pytest -n 4
```

---

## 🔟 Exercícios Práticos

### Exercício 1

Implemente a função `contar_vogais(texto)` que retorna o número de vogais em uma string.
👉 Escreva 4 testes (incluindo texto vazio).

### Exercício 2

Crie a classe `ContaBancaria` com métodos:

* `depositar(valor)`
* `sacar(valor)` (deve lançar `ValueError` se o saldo for insuficiente)
  👉 Escreva testes para validar depósitos, saques e erro ao sacar sem saldo.

### Exercício 3

Crie testes parametrizados para verificar se diferentes palavras são ou não palíndromos (`ana`, `radar`, `python`, `banana`).

### Exercício 4

Use uma fixture que retorna uma lista de dicionários representando produtos.
👉 Escreva um teste que verifica se todos os produtos têm a chave `"preco"`.

---

## ✅ Conclusão

Nesta aula prática vimos:

* Como instalar e rodar testes com Pytest
* Testes de funções, listas e strings
* Testes de classes e exceções
* Fixtures e parametrização
* Plugins úteis (cobertura, execução paralela)