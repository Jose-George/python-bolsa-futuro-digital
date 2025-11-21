# 🧑‍🏫 **Aula: Introdução ao Django e aos Conceitos Fundamentais para Iniciantes**

### ⏱ Duração estimada: **3 horas**

### 📘 Nível: **Iniciante absoluto**

---

## 📍 **Objetivos da Aula**

Ao final da aula, o aluno será capaz de:

* Entender o que é **cliente** e **servidor**.
* Entender o que é um **framework**.
* Compreender o conceito de **aplicação web**.
* Identificar o que é o **Django** e para que serve.
* Criar um projeto Django simples e rodá-lo localmente.
* Entender a estrutura inicial de um projeto Django.

---

# 🕒 **Roteiro da Aula**

| Tópico                                       |
|----------------------------------------------|
| Conceitos fundamentais da web                |
| O que é framework?                           |
| O que é Django? Por que usar?                |
| Preparação do ambiente                       |
| Criando o primeiro projeto Django            |
| Estrutura de diretórios e arquivos           |
| Criando a primeira aplicação e primeira rota |
| Exercícios práticos e revisão                |

---

# 🧩 **1. Conceitos Fundamentais da Web (20 min)**

## 🌐 1.1 Cliente e Servidor

### **Cliente**

É quem faz o pedido.  
Exemplo: seu navegador (Chrome, Firefox, Edge) é o **cliente**.

### **Servidor**

É quem processa o pedido e devolve a resposta.  
Exemplo: quando você acessa o Instagram, um servidor envia o conteúdo da sua conta.

### ⚙ Como funciona?

1. Cliente faz uma requisição (pedido)  
2. Servidor recebe  
3. Servidor processa  
4. Servidor devolve uma resposta  

```

CLIENTE → pedido → SERVIDOR
CLIENTE ← resposta ← SERVIDOR

```

---

## 🌍 1.2 HTTP – O “idioma” da Web

Toda comunicação entre cliente e servidor ocorre via **HTTP** (HyperText Transfer Protocol), o protocolo que define como os dois conversam.

---

### 📌 **O que é HTTP?**

HTTP é um conjunto de regras que define como um cliente (navegador) envia um pedido e como o servidor responde.  
É literalmente a "linguagem da web".

Ele determina:

- como fazer um pedido (requisição)
- como estruturar as informações
- como o servidor deve responder
- como erros são comunicados

---

### 📬 **Requisição HTTP**

Ao acessar um site, o navegador envia uma requisição que contém:

- **Método HTTP** (GET, POST...)
- **URL** (endereço do recurso)
- **Headers** (informações adicionais)
- **Body** (corpo — dados enviados, geralmente em POST)

Exemplo de requisição GET:

```

GET /produtos HTTP/1.1
Host: [www.meusite.com](http://www.meusite.com)
User-Agent: Chrome

```

---

### 📥 **Resposta HTTP**

O servidor responde com:

- **Código de status**
- **Headers**
- **Body** (normalmente HTML ou JSON)

Exemplo:

```

HTTP/1.1 200 OK
Content-Type: text/html

<h1>Lista de Produtos</h1>
```

---

### 🔢 **Principais Códigos HTTP**

| Código      | Significado                  |
| ----------- | ---------------------------- |
| **200**     | OK – requisição bem-sucedida |
| **301/302** | Redirecionamento             |
| **400**     | Erro no pedido do cliente    |
| **401**     | Não autenticado              |
| **403**     | Acesso proibido              |
| **404**     | Não encontrado               |
| **500**     | Erro interno do servidor     |

---

### 📦 **Principais Métodos HTTP**

#### ✔ **GET**

Usado para **buscar dados** (ex.: acessar uma página).

#### ✔ **POST**

Usado para **enviar dados** (ex.: enviar formulário).

#### ✔ **PUT**

Atualiza dados existentes.

#### ✔ **DELETE**

Remove dados.

---

### 🧠 Analogia simples

Imagine um restaurante:

* Você (cliente) chama o garçom.
* O garçom (HTTP) leva seu pedido para a cozinha.
* A cozinha (servidor) prepara.
* O garçom traz sua comida (resposta).

Sem o garçom, você não teria como pedir nada —
e sem HTTP, navegador e servidor não se comunicariam.

---

### 📊 **Por que aprender HTTP antes de Django?**

Porque **Django funciona exatamente como um sistema de requisições e respostas HTTP**.
Cada URL que você cria e cada view que retorna HTML depende desse ciclo.

Entender HTTP facilita todo o resto no Django.

---

# 🧱 **2. O que é um Framework? (20 min)**

Imagine construir uma casa do zero:
Você teria que cortar madeira, criar cimento, montar a estrutura inteira manualmente.

Com um **framework**, é como se a casa viesse:

* com fundação pronta,
* partes estruturais já resolvidas,
* ferramentas prontas para uso.

### ✔ Definição:

**Framework é um conjunto de ferramentas e padrões que facilita o desenvolvimento de aplicações.**

Ele evita que você tenha que reinventar tudo do zero.

## Exemplos de frameworks:

* Para backend: **Django, Flask, FastAPI**
* Para frontend: **React, Angular, Vue**
* Para mobile: **Flutter, React Native**

---

# 🐍 **3. O que é Django? (20 min)**

Django é um **framework web em Python**, criado para facilitar o desenvolvimento de aplicações escaláveis e seguras.

### ✔ Django oferece:

* Servidor web interno
* Sistema de rotas (URLs)
* Conexão com banco de dados
* ORM (mapear objetos para tabelas)
* Painel administrativo automático
* Segurança embutida
* Templates (HTML integrado)
* Autenticação de usuários

### ✔ Por que aprender Django?

* Rápido para desenvolver
* Muito seguro
* Usado por empresas grandes (Instagram começou com Django)
* Código organizado
* Comunidade enorme

---

# ⚙ **4. Preparação do Ambiente (20 min)**

### ✔ 4.1 Verificar Python instalado

```bash
python --version
```

### ✔ 4.2 Criar um ambiente virtual

```bash
python -m venv venv
```

Ativar:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### ✔ 4.3 Instalar Django

```bash
pip install django
```

---

# 🚀 **5. Criando o Primeiro Projeto Django (30 min)**

### ✔ 5.1 Criar um projeto

```bash
django-admin startproject meu_projeto
```

Isso cria uma pasta assim:

```
meu_projeto/
    manage.py
    meu_projeto/
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

### ✔ 5.2 Navegar para o projeto

```bash
cd meu_projeto
```

### ✔ 5.3 Rodar o servidor

```bash
python manage.py runserver
```

Abra no navegador:

```
http://127.0.0.1:8000
```

Você verá a página inicial do Django.

---

# 🗂 **6. Entendendo a Estrutura do Django (30 min)**

## 📄 manage.py

Arquivo principal para rodar comandos, como:

* iniciar servidor
* criar apps
* migrar banco

## 📁 pasta “meu_projeto/”

Contém arquivos de configuração:

* **settings.py** → configurações gerais
* **urls.py** → define rotas
* **wsgi.py** → interface do servidor web
* **asgi.py** → interface para aplicações assíncronas

---

# 🔧 **7. Criando a Primeira Aplicação (30 min)**

No Django, um **projeto** é composto por várias **aplicações**.

### ✔ 7.1 Criar uma aplicação

```bash
python manage.py startapp minha_app
```

Estrutura gerada:

```
minha_app/
    apps.py
    models.py
    views.py
    tests.py
    admin.py
```

### ✔ 7.2 Registrar a aplicação no projeto

No arquivo:

```
meu_projeto/settings.py
```

Adicionar dentro de INSTALLED_APPS:

```python
'minha_app',
```

---

# 📌 **7.3 Criando a Primeira View**

Em:

```
minha_app/views.py
```

Escreva:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Django! Minha primeira página web 🚀")
```

---

# 🌐 **7.4 Criando a Rota (URL)**

No arquivo:

```
meu_projeto/urls.py
```

Adicione:

```python
from django.contrib import admin
from django.urls import path
from minha_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

Agora acesse:

```
http://127.0.0.1:8000
```

Você verá a mensagem:

```
Olá, Django! Minha primeira página web 🚀
```

---

# 📝 **8. Exercícios Práticos (30 min)**

### **1️⃣ Criar páginas novas**

Crie 3 novas funções em `views.py`:

* página de contato
* página sobre
* página “bem-vindo”

Criar rotas para cada uma em `urls.py`.

### **2️⃣ Retornar HTML simples**

Em uma view, retorne:

```html
<h1>Bem-vindo ao meu site</h1>
<p>Este é meu primeiro HTML com Django!</p>
```

### **3️⃣ Desafio**

Criar uma página que retorne:

* título
* parágrafo
* emoji 😄

---

# 🎯 **Recapitulando o que aprendemos**

* Como funciona cliente e servidor
* O que é HTTP
* O que é um framework
* O que é o Django
* Como criar um projeto Django
* Como rodar o servidor
* O que é uma app no Django
* Como criar views e rotas

---

# 🏁 **Conclusão**

Você agora tem a base para começar a desenvolver aplicações web reais usando Django.
Nos próximos passos, você poderá aprender:

* Templates (HTML com Django)
* Modelos e banco de dados
* CRUD
* Painel administrativo
* Autenticação de usuários
