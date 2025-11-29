# 🧱 1. Instalando o Django

Antes de tudo, crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

Ative:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

Agora instale o Django:

```bash
pip install django
```

---

# 🔧 2. Instalando o Django REST Framework

```bash
pip install djangorestframework
```

---

# 🚀 3. Criando o projeto Django

```bash
django-admin startproject apiservice
cd apiservice
```

Estrutura criada:

```
apiservice/
 ├── apiservice/
 ├── manage.py
```

---

# 📁 4. Criando o app

Vamos criar um app chamado **produtos**:

```bash
python manage.py startapp produtos
```

---

# 🧩 5. Ativando o Django REST Framework

Abra:

**apiservice/settings.py**

Adicione no `INSTALLED_APPS`:

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

# 📦 6. Criando um “banco em memória”

Sem banco de dados — vamos usar apenas uma lista Python.

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

# 🗺️ 7. Criando rotas

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

# ▶️ 8. Rodando o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/produtos/
```

---

# 🧪 9. Testando com JSON (Thunder Client/Postman)

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

# 📌 10. Boas Práticas Fundamentais

1. Endpoints sempre no plural

2. Use métodos HTTP corretamente

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

### Rotas obrigatórias:

* **GET** `/usuarios/`
* **POST** `/usuarios/criar/`

### Estrutura em memória:

```python
usuarios = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com"}
]
```

### Regras:

* Ao criar um novo usuário, gere o próximo `id` automaticamente.
* Valide para que todos os campos existam: **id, nome, email**.
* Teste com POST enviando JSON pelo Thunder Client/Postman.

