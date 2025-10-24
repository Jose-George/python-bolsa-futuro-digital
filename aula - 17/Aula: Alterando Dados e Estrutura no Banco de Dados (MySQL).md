# 🧠 Aula 2: Alterando Dados e Estrutura no Banco de Dados (MySQL)

## 🎯 Objetivo

Aprender os comandos SQL responsáveis por **modificar informações e estruturas** dentro do banco de dados:

- `UPDATE`
- `DELETE`
- `ALTER TABLE`
- `DROP TABLE`
- `TRUNCATE`

---

## 🏫 1. Revisão Rápida — Nosso Banco de Dados

Usaremos as mesmas tabelas da **Aula 1**:

```sql
USE EscolaDB;

SELECT * FROM Alunos;
SELECT * FROM Cursos;
SELECT * FROM Matriculas;
````

---

## ✏️ 2. Atualizando dados com `UPDATE`

O comando **`UPDATE`** serve para **alterar registros existentes** em uma tabela.

A estrutura é:

```sql
UPDATE nome_tabela
SET coluna = novo_valor
WHERE condição;
```

⚠️ **Atenção:**
Sempre utilize `WHERE`, senão **todos os registros** da tabela serão alterados.

### Exemplo 1 — Corrigindo o nome de um aluno:

```sql
UPDATE Alunos
SET nome = 'Maria da Silva'
WHERE id = 1;
```

### Exemplo 2 — Alterando a cidade de todos os alunos de "Curitiba" para "Londrina":

```sql
UPDATE Alunos
SET cidade = 'Londrina'
WHERE cidade = 'Curitiba';
```

### Exemplo 3 — Aumentando a carga horária de todos os cursos de 40 para 50 horas:

```sql
UPDATE Cursos
SET carga_horaria = 50
WHERE carga_horaria = 40;
```

---

## 🗑️ 3. Removendo dados com `DELETE`

O comando **`DELETE`** é usado para **excluir registros** da tabela.

```sql
DELETE FROM nome_tabela
WHERE condição;
```

### Exemplo 1 — Apagar o aluno com `id = 4`:

```sql
DELETE FROM Alunos
WHERE id = 4;
```

### Exemplo 2 — Apagar todas as matrículas do curso com `curso_id = 1`:

```sql
DELETE FROM Matriculas
WHERE curso_id = 1;
```

⚠️ **Cuidado:** sem `WHERE`, todos os registros da tabela serão removidos!

---

## 🧱 4. Alterando a estrutura da tabela com `ALTER TABLE`

O comando **`ALTER TABLE`** é usado para **modificar a estrutura** de uma tabela — adicionando, removendo ou alterando colunas.

### Exemplo 1 — Adicionar uma nova coluna `email` na tabela `Alunos`:

```sql
ALTER TABLE Alunos
ADD email VARCHAR(100);
```

### Exemplo 2 — Alterar o tipo de dado da coluna `idade`:

```sql
ALTER TABLE Alunos
MODIFY idade SMALLINT;
```

### Exemplo 3 — Renomear uma coluna:

```sql
ALTER TABLE Alunos
CHANGE cidade cidade_residencia VARCHAR(50);
```

### Exemplo 4 — Excluir uma coluna:

```sql
ALTER TABLE Alunos
DROP COLUMN email;
```

---

## 💣 5. Apagando tabelas e limpando dados

### `DROP TABLE` — Remove **toda a tabela** do banco

```sql
DROP TABLE Matriculas;
```

> ❌ A tabela e todos os dados são **excluídos permanentemente**.

---

### `TRUNCATE` — Limpa **todos os dados**, mas mantém a estrutura da tabela

```sql
TRUNCATE TABLE Alunos;
```

> 💡 A tabela continua existindo, porém **sem registros**.

---

## 🧠 6. Lista de Exercícios

Pratique os conceitos aprendidos com os comandos que **alteram o banco de dados**:

1. Adicione uma nova coluna `telefone` (VARCHAR(20)) na tabela `Alunos`.
2. Atualize o campo `cidade` do aluno com `id = 2` para `'Salvador'`.
3. Aumente a carga horária de todos os cursos que tenham menos de 70 horas para `70`.
4. Exclua o aluno cujo nome é `'Ana Souza'`.
5. Renomeie a coluna `carga_horaria` da tabela `Cursos` para `horas_totais`.
6. Adicione uma nova coluna `status` (VARCHAR(10)) na tabela `Matriculas`.
7. Exclua todas as matrículas relacionadas ao curso `'Banco de Dados'`.
8. Limpe todos os dados da tabela `Cursos`, mas mantenha a estrutura.

---

## 🧩 Dica Importante

Antes de usar comandos que **removem ou alteram** dados (`UPDATE`, `DELETE`, `DROP`, `TRUNCATE`):

1. Faça um **backup** do banco de dados.
2. Use `SELECT` para **testar suas condições** antes de executar.
3. Sempre revise seu `WHERE`!

---

## 🔗 Referência

[https://www.mycompiler.io/pt/new/mysql](https://www.mycompiler.io/pt/new/mysql)
