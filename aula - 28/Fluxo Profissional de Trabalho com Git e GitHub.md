# 🧑‍💻 Aula: **Fluxo Profissional de Trabalho com Git e GitHub**

Bem-vindos! Nesta aula vamos aprender **como organizar um projeto de forma profissional usando Git e GitHub**, seguindo boas práticas usadas no mercado.

Vamos trabalhar com **branches**, **Pull Requests**, **revisão de código** e um **fluxo de desenvolvimento organizado**.

---

## 📌 Objetivo da Aula
Ao final desta aula, você será capaz de:

- Entender a função das branches *main* e *develop*  
- Criar branches de funcionalidades de forma correta  
- Enviar código pelo GitHub utilizando Pull Request  
- Trabalhar em equipe de maneira organizada e profissional  

---

# 📁 1. Estrutura do Projeto no GitHub

### 🔹 **Branches principais**

| Branch | Finalidade |
|-------|------------|
| **main** | Versão estável do projeto (produção). |
| **develop** | Versão em desenvolvimento, onde juntamos novas funcionalidades. |

---

# 🛠️ 2. Como vamos trabalhar no dia a dia

## 2.1 Antes de tudo
📢 **Todos devem enviar o link do seu perfil do GitHub.**  
Eu vou criar um repositório e adicionar vocês como colaboradores.

---

# 🔀 3. Criando branches da forma correta

Sempre que você receber uma tarefa:

1. Atualize seu repositório local  
2. Crie uma branch baseada na **develop**  
3. Dê um nome descritivo à sua branch

### ✔️ Exemplos de nomes de branch:

- `feature/cadastro_usuario`  
- `fix/corrigir_menu`  
- `docs/atualizar_manual`

### 💻 **Comandos usados nesse processo**

#### 1️⃣ Clone o repositório (apenas uma vez):
```bash
git clone https://github.com/usuario/projeto.git
````

#### 2️⃣ Entre na pasta:

```bash
cd projeto
```

#### 3️⃣ Vá para a branch develop:

```bash
git checkout develop
```

#### 4️⃣ Atualize a branch develop:

```bash
git pull origin develop
```

#### 5️⃣ Crie uma nova branch baseada na develop:

```bash
git checkout -b feature/cadastro_usuario
```

---

# 🧩 4. Trabalhando na sua branch

Faça o desenvolvimento da sua tarefa normalmente.
Quando terminar:

### Adicione mudanças:

```bash
git add .
```

### Faça um commit descritivo:

```bash
git commit -m "feat: adicionar tela de cadastro de usuário"
```

### Envie a branch para o GitHub:

```bash
git push origin feature/cadastro_usuario
```

---

# 🔃 5. Abrindo um Pull Request (PR)

Depois que sua branch estiver no GitHub:

1. Entre no repositório no GitHub
2. Vai aparecer um botão: **“Compare & Pull Request”**
3. Garanta que o destino seja **develop**
4. Adicione uma descrição clara do que você fez
5. Envie o PR

Eu irei revisar e aprovar seu código.

---

# ✔️ 6. Revisão e Aprovação

Eu vou:

* Ler seu código
* Fazer comentários (se necessário)
* Aprovar o PR
* Fazer o *merge* da sua branch para a **develop**

---

# 🚀 7. Quando o projeto estiver estável

Assim que a branch **develop** estiver testada e funcionando:

→ faremos o merge da **develop** para a **main**.
Essa será a versão final do projeto.

---

# 🔄 8. Resumo do fluxo

1. Criar branch a partir da **develop**
2. Desenvolver a tarefa
3. Fazer commit + push
4. Abrir Pull Request para a **develop**
5. Revisão e aprovação
6. Merge da **develop** para a **main**

---

# 💡 9. Exemplos adicionais de comandos úteis

## Ver a branch atual:

```bash
git branch
```

## Listar todas as branches remotas:

```bash
git branch -a
```

## Trocar de branch:

```bash
git checkout nome-da-branch
```

## Atualizar branch atual com o repositório online:

```bash
git pull origin minha-branch
```

## Enviar commits para o GitHub:

```bash
git push origin minha-branch
```

## Ver status das alterações:

```bash
git status
```

---

# 📘 10. Material de apoio

👉 Tutorial completo de GitHub (PDF):
[https://www.gileduardo.com.br/ifpr/lp/downloads/tutorial_github.pdf](https://www.gileduardo.com.br/ifpr/lp/downloads/tutorial_github.pdf)

---

# 🎯 Conclusão

Esse fluxo é usado por equipes profissionais e garante:

* organização
* rastreabilidade
* qualidade no código
* facilidade em trabalhar em grupo

