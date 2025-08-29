# 🌱 Aula de Introdução ao Git e GitHub com VS Code Online

## 🎯 Objetivo da Aula

Ao final desta aula você será capaz de:

* Entender o que é **Git** e para que serve.
* Usar o **GitHub** como repositório remoto.
* Integrar o GitHub com o **VS Code online** para gerenciar seus projetos.
* Executar os principais comandos do Git.

---

## 1. O que é o Git?

* **Git** é um sistema de controle de versão.
* Ele permite que você **registre o histórico** do seu projeto e trabalhe em equipe de forma organizada.
* Com o Git você pode:

  * Salvar versões do seu código.
  * Voltar para uma versão anterior se algo der errado.
  * Trabalhar em paralelo com outras pessoas no mesmo projeto.

---

## 2. O que é o GitHub?

* **GitHub** é uma plataforma online que hospeda repositórios Git.
* Ele serve como uma “nuvem” para o seu código.
* Vantagens:

  * Compartilhar projetos com outras pessoas.
  * Trabalhar em equipe em tempo real.
  * Portfólio para mostrar suas habilidades.

---

## 3. Criando uma Conta no GitHub

1. Acesse [https://github.com](https://github.com).
2. Clique em **Sign up** e crie sua conta.
3. Confirme seu e-mail.

---

## 4. Configurando o Ambiente com VS Code Online

O **VS Code online** pode ser usado de duas formas:

* **GitHub Codespaces** (mais avançado, roda direto na nuvem).
* **VS Code Web** (rodando no navegador, acessando repositórios do GitHub).

### Usando VS Code Web:

1. Vá até qualquer repositório no GitHub.
2. Pressione a tecla **`.` (ponto)** → isso abre o repositório no **VS Code Online**.

---

## 5. Criando Seu Primeiro Repositório

1. No GitHub, clique em **New Repository**.
2. Dê um nome, por exemplo: `primeiro-projeto`.
3. Marque a opção **Add a README file**.
4. Clique em **Create repository**.

---

## 6. Clonando o Repositório no VS Code Online

1. No repositório, clique em **Code → HTTPS** e copie o link.
2. No VS Code Online, abra o terminal e digite:

```bash
git clone https://github.com/seu-usuario/primeiro-projeto.git
```

3. Entre na pasta:

```bash
cd primeiro-projeto
```

---

## 7. Principais Comandos Git

No terminal do VS Code, pratique os seguintes comandos:

### 🔹 Configuração inicial

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```

### 🔹 Verificar status

```bash
git status
```

### 🔹 Adicionar arquivos para o controle do Git

```bash
git add nome-do-arquivo
# ou para adicionar todos os arquivos
git add .
```

### 🔹 Salvar uma versão (commit)

```bash
git commit -m "Minha primeira versão"
```

### 🔹 Enviar alterações para o GitHub

```bash
git push origin main
```

### 🔹 Trazer atualizações do GitHub

```bash
git pull origin main
```

---

## 8. Exercício Prático 🎓

1. Crie um repositório chamado `ola-mundo`.
2. Clone no VS Code Online.
3. Crie um arquivo `app.py` com o seguinte conteúdo:

```python
print("Olá, mundo! Meu primeiro código versionado com Git e GitHub.")
```

4. Faça:

   * `git add app.py`
   * `git commit -m "Adiciona app.py"`
   * `git push origin main`

5. Verifique no GitHub se o arquivo foi enviado.

---

## 9. Boas Práticas com Git

* Use **mensagens de commit claras**.
* Sempre sincronize antes de começar (`git pull`).
* Crie **branches** para novas funcionalidades.

---

## 🚀 Conclusão

Parabéns! 🎉
Você aprendeu:

* O que é Git e GitHub.
* Como usar o VS Code online integrado ao GitHub.
* Como versionar e enviar seu primeiro projeto.

