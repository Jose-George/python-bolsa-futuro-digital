# 🧑‍🏫 **Aula 2: HTML, CSS e Primeiro Formulário no Django**

---

# 🌐 **1. HTML – A Estrutura da Página Web**

HTML significa **HyperText Markup Language**.
Ele é responsável por **definir a estrutura** de uma página.

Pense nele como os **tijolos e paredes** de uma casa.

## 🧱 Para que serve o HTML?

Ele organiza o conteúdo da tela:

* títulos
* textos
* botões
* formulários
* imagens
* tabelas

## 📌 Elementos fundamentais do HTML

### **1. `<h1>` até `<h6>` – Títulos**

```html
<h1>Título principal</h1>
<h2>Subtítulo</h2>
```

### **2. `<p>` – Parágrafos**

```html
<p>Esse é um texto comum da página.</p>
```

### **3. `<div>` – Contêiner**

Serve para agrupar elementos.

```html
<div>
  <p>Texto agrupado</p>
</div>
```

### **4. `<form>` – Formulário**

Usado para enviar dados para o servidor.

```html
<form method="POST">
  <input type="text" name="nome">
  <button type="submit">Enviar</button>
</form>
```

### **5. `<input>` – Campos de formulário**

```html
<input type="text" name="produto" placeholder="Digite o nome do produto">
```

---

# 🎨 **2. CSS – A Aparência do Site**

CSS significa **Cascading Style Sheets**.
Ele controla **cor, tamanho, espaçamento, fontes e layout**.

Se o HTML é a estrutura da casa, o **CSS é a decoração**.

## 🎨 Para que serve o CSS?

Com CSS você define:

* cores
* tamanhos
* margens e espaçamentos
* bordas
* alinhamento
* estilos de botões
* aparência geral

## 🎨 Exemplo simples de CSS

```html
<style>
  body {
    background-color: #f5f5f5;
    font-family: Arial;
  }

  h1 {
    color: #333;
  }

  .card {
    background: white;
    padding: 20px;
    border-radius: 10px;
    width: 300px;
  }
</style>
```

### 💡 CSS usa seletores:

| Tipo     | Exemplo      | Explicação                                 |
| -------- | ------------ | ------------------------------------------ |
| elemento | `p {}`       | Estiliza todos `<p>`                       |
| classe   | `.card {}`   | Estiliza apenas elementos com class="card" |
| id       | `#titulo {}` | Estiliza elemento com id="titulo"          |

---

# 🐍 **3. Preparando o Projeto Django**

Vamos criar um projeto chamado **django-primeiro-app**.

No terminal:

```bash
django-admin startproject django_primeiro_app
```

Depois, entre na pasta:

```bash
cd django_primeiro_app
```

Agora crie um app chamado **produtos**:

```bash
python manage.py startapp produtos
```

---

# ⚙ **4. Explicando os Comandos Django**

Vamos entender cada comando importante usado até agora.

---

## 📌 `django-admin startproject`

Cria a estrutura inicial de um projeto Django, contendo:

* configurações
* urls
* arquivos essenciais

É como iniciar uma nova “cidade”.

---

## 📌 `python manage.py startapp`

Cria uma nova aplicação dentro do projeto.

Cada **app** é um módulo responsável por algo:

* produtos
* usuários
* pagamentos
* relatórios
  etc.

---

## 📌 `python manage.py runserver`

Inicia o servidor local.

Ele permite ver o site no navegador:

```
http://127.0.0.1:8000
```

---

## 📌 `python manage.py makemigrations`

Cria arquivos de **migração**, que são instruções para o banco de dados.

Sempre que você modifica um *model*, precisa rodar este comando.

Ele responde:

> “Django, detectei mudanças. Quer criar instruções para atualizar o banco?”

---

## 📌 `python manage.py migrate`

Executa as migrações no banco de dados.

Ou seja, aplica as alterações criando tabelas e colunas.

---

# 📦 **5. Criando o Model de Produto**

No arquivo:

```
produtos/models.py
```

Crie a tabela “Produto”:

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
```

## Agora rode:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 🗂 **6. Criando a View da Lista de Produtos**

No arquivo:

```
produtos/views.py
```

```python
from django.shortcuts import render, redirect
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        Produto.objects.create(nome=nome, preco=preco)
        return redirect('listar_produtos')

    return render(request, 'produtos/form.html')
```

---

# 🌐 **7. Criando URLs**

Crie um arquivo:

```
produtos/urls.py
```

```python
from django.urls import path
from .views import listar_produtos, cadastrar_produto

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('novo/', cadastrar_produto, name='cadastrar_produto'),
]
```

E registre no projeto, em:

```
django_primeiro_app/urls.py
```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
]
```

---

# 🧱 **8. Criando os Templates**

Crie a pasta:

```
produtos/templates/produtos/
```

---

## 📄 **Template: lista.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Produtos</title>

    <style>
        body {
            font-family: Arial;
            background: #f2f2f2;
            padding: 20px;
        }

        .card {
            background: white;
            padding: 15px;
            border-radius: 8px;
            width: 400px;
            margin-bottom: 15px;
        }

        a {
            background: #4CAF50;
            padding: 8px 12px;
            color: white;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h1>Lista de Produtos</h1>

<a href="/produtos/novo/">Cadastrar Produto</a>

{% for produto in produtos %}
    <div class="card">
        <h3>{{ produto.nome }}</h3>
        <p>Preço: R$ {{ produto.preco }}</p>
    </div>
{% empty %}
    <p>Nenhum produto cadastrado.</p>
{% endfor %}

</body>
</html>
```

---

## 📄 **Template: form.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Novo Produto</title>

    <style>
        body {
            font-family: Arial;
            background: #f2f2f2;
            padding: 20px;
        }

        .card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            width: 300px;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-top: 8px;
            border-radius: 5px;
        }

        button {
            margin-top: 10px;
            padding: 10px;
            width: 100%;
            background: blue;
            color: white;
            border-radius: 5px;
        }
    </style>

</head>
<body>

<h1>Novo Produto</h1>

<div class="card">
<form method="POST">
    {% csrf_token %}

    <label>Nome:</label>
    <input type="text" name="nome">

    <label>Preço:</label>
    <input type="number" step="0.01" name="preco">

    <button type="submit">Cadastrar</button>
</form>
</div>

</body>
</html>
```

---

# 📝 **9. Exercício para os Alunos Finalizarem**

Os alunos devem completar o sistema criando **mais dois recursos**:

---

### ✅ **1. Criar um campo “descrição” no model Produto**

* adicionar o campo
* rodar `makemigrations`
* rodar `migrate`
* adicionar no formulário
* mostrar na listagem

---

### ✅ **2. Criar um botão “Excluir produto”**

O aluno deve:

1. Criar uma nova view `excluir_produto`
2. Criar uma rota nova
3. Exibir um botão “Excluir” em cada produto
4. Ao clicar, apagar o produto

---

# 🎉 **Conclusão**

Nesta aula o aluno aprendeu:

* O que é HTML e CSS
* Como estilizar uma página
* O que são URLs, Views e Models
* Como funciona cada comando do Django
* Criar formulários
* Listar e cadastrar produtos

