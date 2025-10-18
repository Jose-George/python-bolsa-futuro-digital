# 🧠 Aula: Introdução ao SQL (MySQL) — Comandos Básicos

## 🎯 Objetivo

Aprender os comandos básicos do SQL para **consultar dados** em um banco de dados MySQL:
- `SELECT`
- `FROM`
- `WHERE`

---

## 🗂️ 1. O que é SQL?

**SQL (Structured Query Language)** é a linguagem usada para **comunicar com bancos de dados relacionais**.  
Com ela, podemos **criar tabelas**, **inserir dados**, **consultar informações**, **atualizar** e **excluir registros**.

---

## 🧩 2. Criando o Banco de Dados e as Tabelas

Antes de fazermos consultas, vamos criar um banco e algumas tabelas de exemplo:

```sql
CREATE DATABASE EscolaDB;
USE EscolaDB;

CREATE TABLE Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    idade INT,
    cidade VARCHAR(50)
);

CREATE TABLE Cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(50),
    carga_horaria INT
);

CREATE TABLE Matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    curso_id INT,
    data_matricula DATE,
    FOREIGN KEY (aluno_id) REFERENCES Alunos(id),
    FOREIGN KEY (curso_id) REFERENCES Cursos(id)
);
````

---

## 📥 3. Inserindo Dados

```sql
INSERT INTO Alunos (nome, idade, cidade)
VALUES 
('Maria Silva', 20, 'São Paulo'),
('João Santos', 22, 'Rio de Janeiro'),
('Ana Souza', 19, 'Belo Horizonte'),
('Carlos Pereira', 25, 'Curitiba');

INSERT INTO Cursos (nome_curso, carga_horaria)
VALUES 
('Banco de Dados', 40),
('Lógica de Programação', 60),
('Desenvolvimento Web', 80);

INSERT INTO Matriculas (aluno_id, curso_id, data_matricula)
VALUES 
(1, 1, '2024-02-15'),
(2, 2, '2024-03-10'),
(3, 1, '2024-04-05'),
(4, 3, '2024-05-20');
```

---

## 🔍 4. Comando `SELECT` e `FROM`

O comando **`SELECT`** é usado para **buscar dados** nas tabelas.

A estrutura básica é:

```sql
SELECT colunas
FROM tabela;
```

### Exemplo 1 — Buscar todos os alunos:

```sql
SELECT * FROM Alunos;
```

`*` significa **todas as colunas** da tabela.

### Exemplo 2 — Buscar apenas nomes e cidades:

```sql
SELECT nome, cidade FROM Alunos;
```

---

## 🎯 5. Filtrando dados com `WHERE`

O comando **`WHERE`** é usado para **filtrar registros** com base em uma condição.

### Exemplo 1 — Alunos com mais de 20 anos:

```sql
SELECT nome, idade 
FROM Alunos
WHERE idade > 20;
```

### Exemplo 2 — Alunos de uma cidade específica:

```sql
SELECT nome, cidade 
FROM Alunos
WHERE cidade = 'São Paulo';
```

### Exemplo 3 — Cursos com carga horária menor que 70:

```sql
SELECT nome_curso, carga_horaria
FROM Cursos
WHERE carga_horaria < 70;
```

---

## 🔗 6. Consultando mais de uma tabela (sem usar JOIN)

Podemos consultar **mais de uma tabela ao mesmo tempo**, listando-as no `FROM`.
Mas precisamos **relacioná-las** usando condições no `WHERE`.

### Exemplo — Mostrar nome do aluno e nome do curso em que ele está matriculado:

```sql
SELECT Alunos.nome AS Nome_Aluno, Cursos.nome_curso AS Curso
FROM Alunos, Cursos, Matriculas
WHERE Alunos.id = Matriculas.aluno_id
  AND Cursos.id = Matriculas.curso_id;
```

➡️ Nesse caso, estamos **cruzando dados** das três tabelas:

* `Alunos` → nome do aluno
* `Cursos` → nome do curso
* `Matriculas` → faz o elo entre as duas

---

## 🧮 7. Outras condições com WHERE

Você pode combinar condições usando `AND` e `OR`.

### Exemplo — Alunos maiores de 20 anos **e** de São Paulo:

```sql
SELECT nome, idade, cidade
FROM Alunos
WHERE idade > 20 AND cidade = 'São Paulo';
```

### Exemplo — Cursos de 40 **ou** 80 horas:

```sql
SELECT nome_curso
FROM Cursos
WHERE carga_horaria = 40 OR carga_horaria = 80;
```

---

## 🧠 8. Lista de Exercícios

Pratique os conceitos aprendidos respondendo às seguintes questões usando **comandos SQL**:

1. Liste **todos os alunos** com suas respectivas cidades.
2. Mostre apenas os **nomes dos cursos** com **carga horária maior que 50 horas**.
3. Exiba os **alunos que moram em Curitiba**.
4. Mostre o **nome e idade dos alunos** com **idade menor que 22 anos**.
5. Liste o **nome do aluno e o nome do curso** em que ele está matriculado.
6. Exiba os **alunos matriculados** no curso **"Banco de Dados"**.
7. Mostre os **cursos com carga horária diferente de 60 horas**.
8. Liste o **nome e cidade** dos alunos **de São Paulo** ou **Rio de Janeiro**.

---

## 🔗 Referência

[https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)
