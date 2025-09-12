# 📘 Aula: Leitura e Escrita de Arquivos em Python (com Exercícios Resolvidos)

## 🔄 Exercícios Resolvidos

---

### 1. **Escrevendo mensagens**

📌 Crie um programa que peça para o usuário digitar três frases e salve todas em um arquivo `frases.txt`.

```python
with open("frases.txt", "w") as arquivo:
    for i in range(3):
        frase = input(f"Digite a frase {i+1}: ")
        arquivo.write(frase + "\n")

print("Frases salvas em frases.txt!")
```

---

### 2. **Lendo mensagens**

📌 Leia o arquivo `frases.txt` e exiba o conteúdo no terminal.

```python
with open("frases.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)
```

---

### 3. **Lista de compras**

📌 Peça ao usuário para digitar itens de compra até ele digitar "sair". Grave todos os itens no arquivo `compras.txt`.

```python
with open("compras.txt", "w") as arquivo:
    while True:
        item = input("Digite um item para a lista de compras (ou 'sair' para encerrar): ")
        if item.lower() == "sair":
            break
        arquivo.write(item + "\n")

print("Lista de compras salva em compras.txt!")
```

---

### 4. **Contando linhas**

📌 Leia um arquivo de texto qualquer e mostre quantas linhas ele possui.

```python
nome_arquivo = input("Digite o nome do arquivo que deseja contar as linhas: ")

with open(nome_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()

print(f"O arquivo {nome_arquivo} possui {len(linhas)} linhas.")
```

---

### 5. **Nomes em ordem**

📌 Crie um arquivo `nomes.txt` com pelo menos 5 nomes. Depois, leia o arquivo, coloque os nomes em ordem alfabética e exiba no terminal.

```python
# Criando arquivo com nomes
with open("nomes.txt", "w") as arquivo:
    arquivo.write("Carlos\n")
    arquivo.write("Ana\n")
    arquivo.write("Bruno\n")
    arquivo.write("Daniela\n")
    arquivo.write("Eduardo\n")

# Lendo e ordenando
with open("nomes.txt", "r") as arquivo:
    nomes = arquivo.readlines()

# Remover quebras de linha
nomes = [nome.strip() for nome in nomes]

# Ordenar
nomes.sort()

print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)
```

---

### 6. **Relatório de notas (extra)**

📌 Crie um arquivo `notas.csv` com nomes de alunos e suas notas. Depois, leia o arquivo e calcule a média das notas.

```python
# Criando arquivo com notas
with open("notas.csv", "w") as arquivo:
    arquivo.write("Nome,Nota\n")
    arquivo.write("Ana,8\n")
    arquivo.write("Bruno,6\n")
    arquivo.write("Carlos,9\n")
    arquivo.write("Daniela,7\n")

# Lendo e calculando média
with open("notas.csv", "r") as arquivo:
    linhas = arquivo.readlines()

soma = 0
contador = 0

# Ignorar a primeira linha (cabeçalho)
for linha in linhas[1:]:
    nome, nota = linha.strip().split(",")
    soma += float(nota)
    contador += 1

media = soma / contador
print(f"A média das notas é: {media:.2f}")
```
