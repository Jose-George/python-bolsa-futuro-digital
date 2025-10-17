# 📝 Lista de Exercícios — MySQL Básico

## 🎯 Objetivo

Fixar o uso dos comandos principais do MySQL:
`CREATE DATABASE`, `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE` e `DELETE`.

Você pode realizar todos os exercícios diretamente no ambiente online:
🔗 [https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)

---

## 🧩 **Exercício 1 — Criar o Banco de Dados**

Crie um banco de dados chamado **loja** e selecione-o para uso.

> 💡 Dica: use os comandos `CREATE DATABASE` e `USE`.

---

## 🧱 **Exercício 2 — Criar a Tabela**

Crie uma tabela chamada **produtos** com os seguintes campos:

| Campo   | Tipo de dado  | Observação                       |
| ------- | ------------- | -------------------------------- |
| id      | INT           | chave primária e auto incremento |
| nome    | VARCHAR(100)  | nome do produto                  |
| preco   | DECIMAL(10,2) | preço do produto                 |
| estoque | INT           | quantidade disponível            |

> 💡 Dica: use `AUTO_INCREMENT` e `PRIMARY KEY` no campo `id`.

---

## ✍️ **Exercício 3 — Inserir Registros**

Insira **três produtos** de sua escolha na tabela `produtos`.
Exemplo (pode criar os seus próprios):

| nome        | preco  | estoque |
| ----------- | ------ | ------- |
| Camiseta    | 59.90  | 30      |
| Calça Jeans | 120.00 | 15      |
| Tênis       | 250.00 | 10      |

> 💡 Dica: use o comando `INSERT INTO ... VALUES (...)`.

---

## 🔍 **Exercício 4 — Consultar os Dados**

Execute consultas simples para visualizar e filtrar os produtos:

1. Mostre **todos os produtos** da tabela.
2. Mostre **apenas o nome e o preço** dos produtos.
3. Mostre apenas os produtos com preço **maior que 100**.

> 💡 Dica: use o comando `SELECT` e o operador `WHERE`.

---

## 🔄 **Exercício 5 — Atualizar e Excluir**

1. Atualize o **estoque** de um dos produtos (ex: aumente em 5 unidades).
2. Exclua **um produto** da tabela.
3. Liste novamente todos os produtos para verificar o resultado.

> 💡 Dica: use `UPDATE ... SET ... WHERE ...` e `DELETE FROM ... WHERE ...`.

---

## ✅ **Objetivo Final**

Ao concluir os 5 exercícios, você terá praticado:

| Comando           | Função               |
| ----------------- | -------------------- |
| `CREATE DATABASE` | Cria um novo banco   |
| `CREATE TABLE`    | Cria uma nova tabela |
| `INSERT`          | Insere dados         |
| `SELECT`          | Consulta dados       |
| `UPDATE`          | Atualiza dados       |
| `DELETE`          | Remove dados         |

---

📘 **Referência para prática:** [https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)

