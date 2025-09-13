# 📚 Aula: Bibliotecas em Python

> **Objetivo:** Entender o que são bibliotecas em Python, como instalá-las, importá-las e utilizá-las na prática.

---

## 1️⃣ O que é uma Biblioteca?

Uma **biblioteca** (ou *module/package*) é um **conjunto de códigos prontos** que outras pessoas já escreveram para resolver problemas comuns.  
Em vez de escrever tudo do zero, você pode **reaproveitar** essas soluções.

➡️ **Exemplo do dia a dia:**  
Pense em uma **caixa de ferramentas**:  
- Você não fabrica o martelo, apenas usa.  
- Em Python, a biblioteca é essa caixa pronta.

---

## 2️⃣ Bibliotecas Padrão (Standard Library)

O Python já vem com várias bibliotecas **embutidas**, conhecidas como **Standard Library**.  
Elas estão disponíveis sem precisar instalar nada.

### Exemplos úteis:
- `math` → Funções matemáticas.
- `datetime` → Trabalhar com datas e horas.
- `os` → Acessar o sistema operacional.
- `random` → Gerar números aleatórios.

```python
import math

print(math.sqrt(16))     # Raiz quadrada
print(math.pi)           # Constante π
````

```python
from datetime import date

hoje = date.today()
print("Data de hoje:", hoje)
```

---

## 3️⃣ Importando Bibliotecas

### Formas de importação:

1. **Importar toda a biblioteca:**

   ```python
   import random
   print(random.randint(1, 10))
   ```

2. **Importar apenas um item específico:**

   ```python
   from math import sqrt
   print(sqrt(25))
   ```

3. **Dar um apelido (alias):**

   ```python
   import numpy as np
   print(np.array([1, 2, 3]))
   ```

> 💡 Usar *alias* é comum para bibliotecas com nomes longos.

---

## 4️⃣ Bibliotecas Externas

Além da Standard Library, existe um **mundo gigante** de bibliotecas criadas pela comunidade.
Exemplos populares:

* `requests` → Fazer requisições web.
* `pandas` → Análise de dados.
* `matplotlib` → Gráficos.
* `flask` → Criar APIs.

Essas precisam ser **instaladas** antes de usar.

---

## 5️⃣ Instalando Bibliotecas

Usamos o **pip** (Python Package Installer), que já vem com o Python.

No terminal ou prompt de comando:

```bash
pip install requests
```

Se quiser instalar uma versão específica:

```bash
pip install requests==2.31.0
```

> ⚠️ Se estiver usando Jupyter Notebook:
>
> ```python
> !pip install requests
> ```

---

## 6️⃣ Onde Encontrar Bibliotecas

O principal repositório é o **[PyPI](https://pypi.org/)** (Python Package Index).

* É como uma loja de aplicativos do Python.
* Pesquise pelo nome da biblioteca e veja como instalar.

---

## 7️⃣ Exemplos Práticos

### 🔹 Exemplo 1: Gerar um número aleatório (biblioteca padrão)

```python
import random

numero = random.randint(1, 100)
print(f"O número sorteado foi {numero}")
```

### 🔹 Exemplo 2: Requisição a um site (biblioteca externa)

```python
import requests

resposta = requests.get("https://api.github.com")
print("Status Code:", resposta.status_code)
print("Conteúdo:", resposta.text[:100])
```

### 🔹 Exemplo 3: Criar gráfico simples

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)
plt.title("Meu primeiro gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
```

---

## 8️⃣ Boas Práticas

* **Leia a documentação**: sempre veja exemplos oficiais.
* **Use ambientes virtuais** (`venv` ou `conda`) para organizar projetos.
* **Atualize suas bibliotecas**:

  ```bash
  pip install --upgrade nome_da_biblioteca
  ```

---

## 9️⃣ Exercícios

1. **Importe a biblioteca `math`** e exiba o seno de 90 graus.
2. Instale a biblioteca `requests` e faça uma requisição para `https://httpbin.org/get`.
3. Gere um número aleatório entre 1 e 50 e mostre na tela.
4. Use `datetime` para imprimir a data e a hora atuais.
5. Crie um gráfico de linha mostrando os números de 0 a 10 e seus quadrados.

---

## 🔑 Resumo da Aula

* **Biblioteca** = código pronto para você reaproveitar.
* **Standard Library** vem com o Python.
* Bibliotecas externas precisam ser instaladas com `pip`.
* Sempre consulte o [PyPI](https://pypi.org/) para novas ferramentas.

> 🏁 **Próximo passo:** experimentar, instalar diferentes bibliotecas e explorar documentações!

