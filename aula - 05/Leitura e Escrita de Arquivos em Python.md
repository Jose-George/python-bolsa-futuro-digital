# 📘 Aula: Leitura e Escrita de Arquivos em Python

## 1. Introdução

Em programação, muitas vezes precisamos **guardar informações em arquivos** e depois **recuperá-las**.
O Python oferece funções simples para manipular arquivos de texto (como `.txt`) ou até arquivos mais complexos (como `.csv`).

---

## 2. Abrindo e Fechando Arquivos

Para trabalhar com arquivos usamos a função `open()`.

### Sintaxe:

```python
arquivo = open("nome_do_arquivo.txt", "modo")
```

### Modos mais usados:

* `"r"` → leitura (read)
* `"w"` → escrita (write, cria ou substitui arquivo)
* `"a"` → acrescentar (append, adiciona ao final)
* `"r+"` → leitura e escrita

⚠️ Sempre que abrir um arquivo, é importante **fechar** depois:

```python
arquivo.close()
```

---

## 3. Escrevendo em Arquivos

### Exemplo 1: Criando um arquivo e escrevendo texto

```python
arquivo = open("exemplo.txt", "w")
arquivo.write("Olá, mundo!\n")
arquivo.write("Esta é minha primeira escrita em arquivo.\n")
arquivo.close()
```

Isso cria o arquivo **exemplo.txt** com duas linhas de texto.

---

## 4. Lendo Arquivos

### Exemplo 2: Lendo todo o conteúdo

```python
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```

Saída:

```
Olá, mundo!
Esta é minha primeira escrita em arquivo.
```

---

### Exemplo 3: Lendo linha por linha

```python
arquivo = open("exemplo.txt", "r")
linha1 = arquivo.readline()
linha2 = arquivo.readline()
print("Linha 1:", linha1)
print("Linha 2:", linha2)
arquivo.close()
```

---

### Exemplo 4: Lendo todas as linhas em uma lista

```python
arquivo = open("exemplo.txt", "r")
linhas = arquivo.readlines()
print(linhas)
arquivo.close()
```

Saída:

```python
['Olá, mundo!\n', 'Esta é minha primeira escrita em arquivo.\n']
```

---

## 5. Acrescentando Conteúdo

### Exemplo 5: Usando `"a"`

```python
arquivo = open("exemplo.txt", "a")
arquivo.write("Nova linha adicionada ao final!\n")
arquivo.close()
```

---

## 6. Usando `with` (Boa Prática)

O `with` fecha o arquivo automaticamente.

### Exemplo 6: Escrevendo com `with`

```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
```

### Exemplo 7: Lendo com `with`

```python
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip remove \n
```

---

## 7. Trabalhando com Listas e Arquivos

### Exemplo 8: Escrevendo lista em arquivo

```python
nomes = ["Ana", "Bruno", "Carlos", "Daniela"]

with open("nomes.txt", "w") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")
```

### Exemplo 9: Lendo lista de arquivo

```python
with open("nomes.txt", "r") as arquivo:
    lista_nomes = arquivo.readlines()

print(lista_nomes)
```

---

## 8. Trabalhando com Arquivos CSV Simples

Arquivos **CSV** (valores separados por vírgula) são comuns em planilhas.

### Exemplo 10: Escrevendo CSV manualmente

```python
with open("alunos.csv", "w") as arquivo:
    arquivo.write("Nome,Idade\n")
    arquivo.write("Ana,20\n")
    arquivo.write("Bruno,22\n")
```

### Exemplo 11: Lendo CSV

```python
with open("alunos.csv", "r") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha.strip())
```

---

## 9. Exercícios para Praticar 📝

1. **Escrevendo mensagens:**
   Crie um programa que peça para o usuário digitar três frases e salve todas em um arquivo `frases.txt`.

2. **Lendo mensagens:**
   Leia o arquivo `frases.txt` e exiba o conteúdo no terminal.

3. **Lista de compras:**
   Peça ao usuário para digitar itens de compra até ele digitar "sair". Grave todos os itens no arquivo `compras.txt`.

4. **Contando linhas:**
   Leia um arquivo de texto qualquer e mostre quantas linhas ele possui.

5. **Nomes em ordem:**
   Crie um arquivo `nomes.txt` com pelo menos 5 nomes. Depois, leia o arquivo, coloque os nomes em ordem alfabética e exiba no terminal.

6. **Relatório de notas (extra):**
   Crie um arquivo `notas.csv` com nomes de alunos e suas notas. Depois, leia o arquivo e calcule a média das notas.
