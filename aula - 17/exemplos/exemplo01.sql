

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
(9, 10, '2024-02-15'),
(10, 11, '2024-03-10'),
(11, 10, '2024-04-05'),
(12, 12, '2024-05-20');





select * from Matriculas;
select * from Cursos;
select * from Alunos;



SELECT Alunos.nome AS Nome_Aluno, Alunos.idade,  Cursos.nome_curso AS Curso,
Cursos.carga_horaria
FROM Alunos, Cursos, Matriculas
WHERE Alunos.id = Matriculas.aluno_id
  AND Cursos.id = Matriculas.curso_id;
  
  
  
SELECT nome, idade, cidade
FROM Alunos
WHERE idade >= 20 AND cidade = 'São Paulo';


SELECT nome_curso
FROM Cursos
WHERE carga_horaria = 40 OR carga_horaria = 80;