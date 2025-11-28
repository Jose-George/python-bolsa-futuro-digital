# 🧪 Aula Completa: **Introdução a WebServices (com Django REST Framework)**

**Nível:** Iniciantes absolutos
**Objetivo:** Ensinar do zero o que é um WebService, por que existe, como funciona, seus formatos, o conceito de API, REST, RESTful e criar um WebService completo usando **Django REST Framework**.

---

# 📌 1. O que é um WebService? (30 min)

## 📖 Definição simples

Um **WebService** é um serviço disponível na web que permite que **sistemas conversem entre si**.
Ele permite que dois programas troquem informações automaticamente, sem interação humana direta.

### Exemplos reais:

* Previsão do tempo — um site consulta outro sistema.
* Uber/99 — usam WebServices do Google Maps.
* E-commerce — calcula frete usando serviços dos Correios.
* Bancos — trocam dados entre vários sistemas internos via serviços.

---

## 🧠 Por que WebServices existem?

Porque nenhum sistema vive isolado.

Eles permitem:

* 🔄 Comunicação automática entre sistemas
* 🤖 Automação de processos
* 🌐 Integração entre aplicações
* 📡 Troca estruturada de dados

Um WebService é a maneira *padronizada* de permitir que sistemas conversem.

---

# 📌 2. Modelo Cliente–Servidor (30 min)

## 🌍 Como funciona?

Quase todos os WebServices funcionam no modelo:

* **Cliente** → quem faz o pedido
* **Servidor** → quem responde

Fluxo:

1. Cliente envia uma **requisição** (request).
2. Servidor processa.
3. Servidor devolve uma **resposta** (response).

Exemplo:

```
Cliente → GET /produtos
Servidor → [ {…}, {…} ]
```

---

# 📌 3. O que é HTTP?

É o protocolo que controla as requisições.

### Métodos mais importantes:

* **GET** → buscar dados
* **POST** → criar dados
* **PUT** → atualizar
* **DELETE** → remover

---

# 📌 4. O que é uma API? (20 min)

API significa **Application Programming Interface**.

É o conjunto de regras que define como um sistema expõe seus serviços para serem usados por outros sistemas.

### Importante:

* API ≠ WebService
* API é o *contrato*
* WebService é o *meio de comunicação*

---

# 📌 5. O que é REST? E RESTful? (30 min)

## 🌱 REST

REST é um **estilo de arquitetura** para criação de WebServices.

Princípios:

1. **Baseado em recursos** (produtos, pedidos, usuários)
2. **Cada recurso tem uma URL**
3. **Métodos HTTP representam ações**
4. **Geralmente usa JSON**
5. **Stateless** → sem guardar estado entre requisições

## 🌿 RESTful

Um WebService RESTful é aquele que segue as regras REST corretamente.

Exemplo:

```
GET /produtos
POST /produtos
GET /produtos/1
PUT /produtos/1
DELETE /produtos/1
```

---

# 📌 6. Formatos de Dados: JSON e XML (20 min)

## 🟨 JSON

O formato mais usado atualmente.

```json
{
  "nome": "Camiseta",
  "preco": 49.90
}
```

## 🟦 XML

Formato mais antigo, ainda usado em governo e bancos:

```xml
<produto>
  <nome>Camiseta</nome>
  <preco>49.90</preco>
</produto>
```

---

# 📌 7. URL, Rota e Endpoint (15 min)

* **URL** → endereço completo
* **Rota** → caminho para um recurso
* **Endpoint** → rota + método HTTP

Exemplo:

```
POST /produtos → criar um produto
```

---

# 🚀 8. Criando o Primeiro WebService com Django REST Framework (60 min)

Agora vamos substituir o Flask por algo muito mais profissional:
📌 **Django + Django REST Framework**

---

# 📥 8.1 Instalando Django e DRF

```bash
pip install django djangorestframework
```

---

# 📁 8.2 Criando o projeto

```bash
django-admin startproject apiservice
cd apiservice
```

---

# 📁 8.3 Criando o app

```bash
python manage.py startapp produtos
```

---

# 🧩 8.4 Ativando o Django REST Framework

Abra:

**apiservice/settings.py**

Adicione:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST Framework
    'rest_framework',

    # Nosso app
    'produtos',
]
```

---

# 📦 8.5 Criando um "banco em memória"

➡️ Para simplificar, não vamos usar banco de dados.
➡️ Assim como no Flask, criaremos uma lista Python.

Abra:

**produtos/views.py**

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Banco de dados em memória
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 49.90},
    {"id": 2, "nome": "Tênis", "preco": 199.90},
]

@api_view(["GET"])
def listar_produtos(request):
    return Response(produtos)

@api_view(["POST"])
def criar_produto(request):
    novo = request.data
    novo["id"] = len(produtos) + 1
    produtos.append(novo)
    return Response(novo, status=201)
```

---

# 🗺️ 8.6 Criando rotas

Abra:

**apiservice/urls.py**

```python
from django.contrib import admin
from django.urls import path
from produtos.views import listar_produtos, criar_produto

urlpatterns = [
    path('admin/', admin.site.urls),

    path("produtos/", listar_produtos),
    path("produtos/criar/", criar_produto),
]
```

---

# ▶️ 8.7 Rodando

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/produtos/
```

---

# 🧪 9. Testando usando JSON (Postman/Thunder Client)

### Criar produto (POST)

URL:

```
http://127.0.0.1:8000/produtos/criar/
```

Body JSON:

```json
{
  "nome": "Bermuda",
  "preco": 89.90
}
```

---

# 📌 10. Boas Práticas Fundamentais (20 min)

1. Endpoints sempre no plural
2. Use os métodos HTTP corretamente
3. Sempre retorne JSON
4. Use códigos HTTP:

   * 200 → OK
   * 201 → Created
   * 400 → Bad Request
   * 404 → Not Found
   * 500 → Server Error
5. Não exponha senhas
6. Valide dados sempre

---

# 📌 11. Tabela de Referência Rápida

### Métodos HTTP

| Método | Uso                    |
| ------ | ---------------------- |
| GET    | Buscar dados           |
| POST   | Criar                  |
| PUT    | Atualizar              |
| PATCH  | Atualizar parcialmente |
| DELETE | Remover                |

### Códigos HTTP

| Código | Significado            |
| ------ | ---------------------- |
| 200    | Sucesso                |
| 201    | Criado                 |
| 400    | Requisição inválida    |
| 404    | Recurso não encontrado |
| 500    | Erro interno           |

---

# 📝 12. Exercício Final

Crie um WebService usando Django REST Framework com:

### Recurso: **Usuários**

### Rotas:

* **GET** `/usuarios/`
* **POST** `/usuarios/criar/`

### Estrutura (em memória):

```python
usuarios = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com"}
]
```

### Campos obrigatórios:

* id
* nome
* email

Teste com POST enviando JSON.

