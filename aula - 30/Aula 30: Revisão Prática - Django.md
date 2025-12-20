# Aula 30: Revisão Prática - Django Rest Framework

Bem-vindo à Aula 30! Hoje faremos uma revisão prática intensiva sobre **Django Rest Framework (DRF)**. O foco é consolidar conceitos fundamentais e praticar o fluxo completo de criação de uma API.

## Objetivos da Aula
- Revisar a criação de projetos Django e configuração do DRF.
- Consolidar o entendimento sobre **ViewSets** e **Routers**.
- Implementar um **CRUD completo** (Create, Read, Update, Delete).
- Aprender a utilizar **Filtros** para refinar as consultas na API.

---

## 1. Criação do Projeto

Vamos começar do zero. Abra seu terminal e siga os passos abaixo.

### 1.1. Preparar o Ambiente

1.  Crie a pasta do projeto (se ainda não estiver nela) e entre nela:
    ```bash
    mkdir projeto_revisao_drf
    cd projeto_revisao_drf
    ```

2.  Crie o ambiente virtual:
    ```bash
    python -m venv venv
    ```

3.  Ative o ambiente virtual:
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux:**
      ```bash
      source venv/bin/activate
      ```

### 1.2. Instalação das Dependências

Instale o Django, o Django Rest Framework e o django-filter (que usaremos mais tarde):

```bash
pip install django djangorestframework django-filter
```

### 1.3. Criar o Projeto Django

Crie o projeto chamado `loja`:

```bash
django-admin startproject loja .
```
*(O "ponto" no final cria o projeto no diretório atual, sem criar uma subpasta extra)*

### 1.4. Validar a Criação

Sua estrutura deve estar assim:

```text
projeto_revisao_drf/
├── loja/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/
└── manage.py
```

---

## 2. Criação do App

Vamos criar um app para gerenciar **Produtos** de uma loja, um exemplo clássico para CRUD.

### 2.1. Criar o App

No terminal, execute:

```bash
python manage.py startapp produtos
```

### 2.2. Registrar Apps no `settings.py`

Abra o arquivo `loja/settings.py` e adicione `'rest_framework'`, `'django_filters'` e o nosso app `'produtos'` na lista `INSTALLED_APPS`:

```python
# loja/settings.py

INSTALLED_APPS = [
    # ... apps padrão do django ...
    'django.contrib.staticfiles',

    # Terceiros
    'rest_framework',
    'django_filters',

    # Meus Apps
    'produtos',
]
```

### 2.3. Criar o Modelo

Vamos criar um modelo simples em `produtos/models.py`:

```python
# produtos/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    em_estoque = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
```

### 2.4. Migrar o Banco de Dados

Sempre que criamos ou alteramos modelos, precisamos criar e rodar as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 3. Configuração do Django Rest Framework

Agora vamos conectar nosso modelo ao mundo das APIs conversando em JSON.

### 3.1. Criar o Serializer

O **Serializer** transforma objetos Python (do modelo) em JSON e valida os dados recebidos.

Crie um arquivo chamado `serializers.py` dentro da pasta `produtos`:

```python
# produtos/serializers.py
from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'  # Ou liste os campos: ['id', 'nome', 'preco', ...]
```

---

## 4. ViewSet

O **ViewSet** lida com a lógica das requisições (GET, POST, PUT, DELETE) de forma automática para operações padrão.

### 4.1. Criar o ViewSet

Abra `produtos/views.py`:

```python
# produtos/views.py
from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
```

**O que o `ModelViewSet` faz?**
Ele já implementa magicamente:
- `list` (GET /produtos/): Lista todos
- `create` (POST /produtos/): Cria um novo
- `retrieve` (GET /produtos/1/): Detalhes de um item
- `update` (PUT /produtos/1/): Atualiza tudo
- `partial_update` (PATCH /produtos/1/): Atualiza parcial
- `destroy` (DELETE /produtos/1/): Remove item

### 4.2. Configurar as Rotas

Vamos usar o `DefaultRouter` para gerar as URLs automaticamente.

Abra `loja/urls.py`:

```python
# loja/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from produtos.views import ProdutoViewSet

# Criação do Router
router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Inclui todas as rotas do router
]
```

---

## 5. CRUD Completo

Agora vamos rodar o servidor e testar.

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/api/produtos/](http://127.0.0.1:8000/api/produtos/)

### 5.1. Testando as Operações

Use a interface navegável do DRF (no navegador) ou o Postman/Insomnia.

1.  **Criar (POST):**
    - Preencha o formulário HTML na parte inferior da página.
    - JSON Exemplo:
      ```json
      {
          "nome": "Notebook Gamer",
          "preco": "4500.00",
          "em_estoque": true
      }
      ```
    - Clique em "POST".

2.  **Listar (GET):**
    - Veja a lista de objetos criados na página principal.

3.  **Detalhar (GET ID):**
    - Clique no link do ID ou vá para `/api/produtos/1/`.

4.  **Atualizar (PUT/PATCH):**
    - Na página de detalhe (`/1/`), altere os valores no formulário e clique em PUT.

5.  **Deletar (DELETE):**
    - Na página de detalhe, clique no botão "DELETE".

---

## 6. Filtros com ViewSet

Muitas vezes queremos buscar produtos específicos, por exemplo, "todos os produtos com preço maior que 100".

### 6.1. Configuração Global (Settings)

No `loja/settings.py`, adicione a configuração padrão do DRF para usar o `django-filter`:

```python
# loja/settings.py

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}
```

### 6.2. Habilitar no ViewSet

Volte em `produtos/views.py` e adicione os campos de filtro:

```python
# produtos/views.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    # Atributos de filtro
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # 1. Filtros exatos (ex: ?em_estoque=true)
    filterset_fields = ['em_estoque']
    
    # 2. Busca textual (ex: ?search=gamer)
    search_fields = ['nome', 'descricao']
    
    # 3. Ordenação (ex: ?ordering=preco)
    ordering_fields = ['preco', 'nome']
```

### 6.3. Testando Filtros

Recarregue a página `/api/produtos/` e teste na URL:

- **Filtrar por estoque:** `?em_estoque=true`
- **Buscar por nome:** `?search=gamer`
- **Ordenar por preço:** `?ordering=preco` (ou `?ordering=-preco` para decrescente)

---

## 7. Lista de Exercícios

Agora é sua vez de praticar!

### Exercício 1: Categoria
1.  Adicione o modelo `Categoria` e a chave estrangeira em `produtos/models.py`. Use o código abaixo como base:
    ```python
    class Categoria(models.Model):
        nome = models.CharField(max_length=50)

        def __str__(self):
            return self.nome

    # Lembre-se de adicionar a ForeignKey no modelo Produto:
    # categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    ```
2.  Adicione um campo `categoria` (ForeignKey) no modelo `Produto` (como mostrado acima).
3.  Atualize o banco (`makemigrations` e `migrate`).
4.  Crie `CategoriaSerializer` e `CategoriaViewSet`.
5.  Registre a rota `/categorias` no `router`.

### Exercício 2: Filtro por Categoria
1.  Adicione `categoria` no `filterset_fields` do `ProdutoViewSet`.
2.  Teste filtrar produtos de uma categoria específica (ex: `?categoria=1`).

### DESAFIO: Validação
1.  No `ProdutoSerializer`, adicione uma validação customizada (`validate_preco`) para impedir que um produto tenha preço negativo ou zero.
2.  Teste tentar criar um produto com preço `-10`.

---

**Parabéns!** Você completou a revisão prática da Aula 30.
Se tiver dúvidas, consulte a documentação oficial: [django-rest-framework.org](https://www.django-rest-framework.org/)
