# Aula: Engenharia de Software – Testes de Software com Python

## 🎯 Objetivos da Aula

* Entender a importância dos testes na Engenharia de Software.
* Conhecer os diferentes tipos de testes de software.
* Aprender a escrever testes automatizados em Python.
* Praticar conceitos com exercícios.

---

## 1. Introdução aos Testes de Software

### O que são testes?

Testes de software são atividades que verificam se um sistema funciona conforme o esperado, garantindo **qualidade**, **segurança** e **manutenção do código**.

### Por que testar?

* Evitar bugs em produção.
* Reduzir custos de manutenção.
* Melhorar a confiabilidade do software.
* Aumentar a confiança dos desenvolvedores em refatorar o código.

👉 *Uma frase importante na Engenharia de Software:*

> "Quanto antes encontramos um erro, mais barato é corrigi-lo."

---

## 2. Tipos de Testes de Software

### 2.1 Testes Manuais

* Feitos por humanos, executando cenários de uso.
* Mais caros e lentos, porém úteis em testes exploratórios.

### 2.2 Testes Automatizados

* Especificados em código.
* Rápidos, repetíveis e integráveis em pipelines de CI/CD.

---

### 2.3 Classificação dos Testes

#### a) Testes de Unidade (Unit Tests)

* Testam **pequenas partes do código** (funções, métodos, classes).
* Exemplo: verificar se a função `soma(2, 3)` retorna `5`.

Exemplo em **Python**:

```python
def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(10, 5) == 15
```

---

#### b) Testes de Integração

* Verificam se **módulos diferentes funcionam bem juntos**.
* Exemplo: testar se um repositório de banco de dados grava e recupera corretamente.

```python
class BancoDeDados:
    def __init__(self):
        self.dados = {}

    def salvar(self, chave, valor):
        self.dados[chave] = valor

    def buscar(self, chave):
        return self.dados.get(chave)

def test_integra_banco():
    db = BancoDeDados()
    db.salvar("usuario1", "George")
    assert db.buscar("usuario1") == "George"
```

---

#### c) Testes de Sistema (End-to-End)

* Testam o sistema completo como o usuário final o utilizaria.
* Exemplo: usar um framework de testes web (como Selenium ou Playwright) para verificar uma aplicação inteira.

```python
# Exemplo simples (simulação, sem Selenium real)
def login(usuario, senha):
    return usuario == "admin" and senha == "123"

def test_login():
    assert login("admin", "123") == True
    assert login("user", "123") == False
```

---

#### d) Testes de Regressão

* Garantem que **novas alterações não quebrem funcionalidades antigas**.
* Geralmente reexecutam os testes anteriores.

---

#### e) Testes de Performance

* Medem **tempo de execução**, **uso de memória** e **resposta sob carga**.

Exemplo com Python:

```python
import time

def funcao_lenta():
    time.sleep(0.5)
    return True

def test_performance():
    inicio = time.time()
    resultado = funcao_lenta()
    fim = time.time()
    assert resultado is True
    assert (fim - inicio) < 1  # deve rodar em menos de 1s
```

---

#### f) Testes de Aceitação

* Verificam se o sistema **atende aos requisitos do cliente**.
* Normalmente escritos em linguagem próxima ao negócio.

Exemplo simplificado:

```python
def calcular_desconto(valor):
    if valor > 100:
        return valor * 0.9  # 10% desconto
    return valor

def test_aceitacao_desconto():
    assert calcular_desconto(200) == 180
    assert calcular_desconto(50) == 50
```

---

#### g) Testes de Segurança

* Avaliam se o sistema é resistente a ataques.
* Exemplo: impedir **SQL Injection**.

```python
def autenticar(usuario, senha):
    # Simulação de segurança
    if "'" in usuario or "'" in senha:
        return "Tentativa de ataque detectada!"
    if usuario == "admin" and senha == "123":
        return "Login autorizado"
    return "Acesso negado"

def test_seguro():
    assert autenticar("admin", "123") == "Login autorizado"
    assert autenticar("' OR 1=1 --", "123") == "Tentativa de ataque detectada!"
```

---

## 3. Ferramentas de Testes em Python

* **unittest** → nativo do Python.
* **pytest** → mais simples e popular, recomendado.
* **coverage** → mede a cobertura dos testes.
* **tox** → automação de ambientes de testes.

Exemplo com `pytest`:

```python
# arquivo: calculadora.py
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

# arquivo: test_calculadora.py
from calculadora import soma, subtrai

def test_soma():
    assert soma(3, 2) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2
```

Rodando os testes no terminal:

```bash
pytest test_calculadora.py
```

---

## 4. Boas Práticas de Testes

1. Nomeie testes de forma clara (`test_soma_dois_numeros`).
2. Teste **um cenário por teste**.
3. Escreva testes **antes ou junto com o código** (TDD).
4. Use mocks/stubs para isolar dependências externas.
5. Automatize os testes no pipeline (CI/CD).

---

## 5. Exercícios de Fixação

### Exercício 1 – Unit Test Básico

Crie uma função `eh_par(numero)` que retorna `True` se o número for par.

* Escreva **3 testes unitários** cobrindo casos positivos e negativos.

---

### Exercício 2 – Teste de Integração

Implemente uma classe `CarrinhoDeCompras` com métodos:

* `adicionar_item(nome, preco)`
* `total()`

Escreva testes que:

1. Adicionem produtos.
2. Validem o valor total.

---

### Exercício 3 – Teste de Regressão

Implemente uma função `fatorial(n)` e escreva testes.

* Depois, altere a função para incluir a regra: `fatorial(0) = 1`.
* Verifique se os testes ainda passam (regressão).

---

### Exercício 4 – Teste de Performance

Crie uma função que gera uma lista de 1 milhão de números.

* Escreva um teste que garanta que o tempo de execução é menor que **2 segundos**.

---

### Exercício 5 – Aceitação

Implemente uma função `calcular_frete(peso, distancia)` com a regra:

* Até 10kg → R$ 5 por km.
* Acima de 10kg → R$ 7 por km.

Crie testes de aceitação para validar os requisitos.

---

### Exercício 6 – Segurança

Implemente uma função de autenticação que rejeita senhas menores que 8 caracteres.

* Escreva testes cobrindo cenários de sucesso e falha.

---

### Exercício 7 – Teste com Mock

Simule uma classe `ServicoEmail` com um método `enviar_email(destinatario, mensagem)`.

* Escreva um teste que use **mock** para garantir que o método é chamado corretamente, sem de fato enviar e-mails.

---

## 6. Conclusão

* Testes são parte fundamental da **Engenharia de Software**.
* Existem **diversos tipos de testes**, cada um com um objetivo específico.
* Python fornece ferramentas poderosas como **pytest** para automação.
* A prática de escrever e manter testes melhora a **qualidade, segurança e manutenibilidade** do código.

