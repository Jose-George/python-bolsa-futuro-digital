# 🧠 Aula 3: Introdução ao MySQL e Primeiros Comandos SQL

## 🎯 Objetivo da Aula

Aprender a **criar, visualizar e manipular dados em um banco de dados MySQL**, entendendo os comandos básicos da linguagem SQL (Structured Query Language).

Nesta aula você vai:

* Criar seu **primeiro banco de dados** e **tabelas** no MySQL;
* Inserir e visualizar registros;
* Atualizar e excluir informações;
* Praticar com exemplos e exercícios guiados.

---

## 🧩 1. O Que é o MySQL?

O **MySQL** é um dos **bancos de dados relacionais** mais populares do mundo — gratuito, rápido e confiável.

Ele utiliza a linguagem **SQL (Structured Query Language)** para **criar, consultar e gerenciar** os dados.

> 💡 É amplamente usado em sites, aplicativos e sistemas corporativos — desde projetos pequenos até grandes plataformas como WordPress, YouTube e Facebook.

---

## ⚙️ 2. Estrutura Básica

Antes de começar, veja como o MySQL organiza as informações:

```
Servidor MySQL
 ├── Banco de Dados (ex: biblioteca)
 │    ├── Tabela (ex: livros)
 │    │    ├── Coluna (ex: título, autor, ano)
 │    │    ├── Registro (ex: "Dom Casmurro", "Machado de Assis", 1899)
```

---
## 💡 Comandos SQL mais comuns no MySQL

| Categoria             | Comandos                     |
| --------------------- | ---------------------------- |
| **Definição (DDL)**   | `CREATE`, `ALTER`, `DROP`    |
| **Manipulação (DML)** | `INSERT`, `UPDATE`, `DELETE` |
| **Consulta (DQL)**    | `SELECT`                     |
| **Controle (DCL)**    | `GRANT`, `REVOKE`            |


---

## 🧱 3. Criando um Banco de Dados

```sql
CREATE DATABASE biblioteca;
```

Esse comando cria um banco chamado **biblioteca**.

Para usar o banco recém-criado:

```sql
USE biblioteca;
```

---

## 📄 4. Criando Tabelas

Vamos criar uma tabela chamada **livros**:

```sql
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ano_publicacao INT
);
```

Explicando:

* `id`: número único que identifica cada livro;
* `AUTO_INCREMENT`: aumenta automaticamente o valor do id;
* `PRIMARY KEY`: define o identificador principal da tabela;
* `VARCHAR(100)`: texto com até 100 caracteres;
* `INT`: número inteiro.

---

## ✍️ 5. Inserindo Dados

Agora, vamos inserir alguns livros:

```sql
INSERT INTO livros (titulo, autor, ano_publicacao)
VALUES
('Dom Casmurro', 'Machado de Assis', 1899),
('O Alienista', 'Machado de Assis', 1882),
('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 1881),
('Capitães da Areia', 'Jorge Amado', 1937);
```

---

## 🔍 6. Consultando os Dados

Para ver todos os livros cadastrados:

```sql
SELECT * FROM livros;
```

> `*` significa “todas as colunas”.

Para ver apenas o título e o autor:

```sql
SELECT titulo, autor FROM livros;
```

Para filtrar apenas livros de **Machado de Assis**:

```sql
SELECT * FROM livros WHERE autor = 'Machado de Assis';
```

---

## 🔄 7. Atualizando Dados

Se o ano de publicação estiver incorreto:

```sql
UPDATE livros
SET ano_publicacao = 1938
WHERE titulo = 'Capitães da Areia';
```

> ⚠️ Use sempre o **WHERE** ao atualizar, para não modificar todos os registros da tabela!

---

## ❌ 8. Excluindo Dados

Para apagar um livro específico:

```sql
DELETE FROM livros WHERE id = 2;
```

Para apagar **todos os registros**, mas manter a tabela:

```sql
DELETE FROM livros;
```

Para apagar a tabela inteira:

```sql
DROP TABLE livros;
```

---

## 📊 9. Criando Outra Tabela: Usuários

Vamos criar uma tabela de **usuários da biblioteca**:

```sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    idade INT
);
```

Inserindo alguns usuários:

```sql
INSERT INTO usuarios (nome, email, idade)
VALUES
('Maria Silva', 'maria@gmail.com', 30),
('João Pereira', 'joao@gmail.com', 25),
('Ana Costa', 'ana@gmail.com', 22);
```

Consultando:

```sql
SELECT * FROM usuarios;
```

---

## 🧠 10. Resumo da Aula

| Conceito      | Exemplo                              |
| ------------- | ------------------------------------ |
| Criar Banco   | `CREATE DATABASE nome;`              |
| Usar Banco    | `USE nome;`                          |
| Criar Tabela  | `CREATE TABLE ...`                   |
| Inserir Dados | `INSERT INTO tabela VALUES ...`      |
| Consultar     | `SELECT * FROM tabela;`              |
| Filtrar       | `SELECT ... WHERE ...;`              |
| Atualizar     | `UPDATE tabela SET campo = valor;`   |
| Deletar       | `DELETE FROM tabela WHERE id = ...;` |

---

## 🧩 11. Exercícios de Fixação

### 🧱 Parte 1 — Estrutura

1. Crie um banco de dados chamado **escola**.

2. Crie uma tabela **alunos** com os campos:

   * `id` (INT, chave primária, auto incremento)
   * `nome` (VARCHAR)
   * `idade` (INT)
   * `serie` (VARCHAR)

3. Insira **5 alunos** com diferentes idades e séries.

---

### 🔍 Parte 2 — Consultas

4. Exiba **todos os alunos** cadastrados.
5. Exiba apenas os **nomes e idades**.
6. Exiba os alunos da série “8º Ano”.
7. Atualize a idade de um aluno.
8. Exclua um aluno da tabela.

---

### 💡 Desafio Extra

Crie uma nova tabela chamada **professores** e adicione alguns registros.
Depois, tente listar os professores da sua escola fictícia.

---

## 🧭 12. Dica de Prática

Você pode testar **todos os comandos MySQL diretamente online**, sem precisar instalar nada:

🔗 [https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)

---

## 🗝️ Conclusão

Nesta aula, você aprendeu a **criar e manipular dados no MySQL**, dominando os comandos essenciais:

* `CREATE`, `INSERT`, `SELECT`, `UPDATE` e `DELETE`;
* Como estruturar e consultar tabelas simples;
* E como praticar com segurança em um ambiente online.


---

📘 **Treinar:** [https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)
