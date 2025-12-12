# 🧠 Aula: Relacionamentos entre Modelos no Django REST Framework

**Duração:** 1h  
**Nível:** Iniciante  
**Tecnologias:** Python, Django, Django REST Framework  
**Pré-requisitos:**  
✅ Conhecimento básico de Django  
✅ Conhecimento básico de Django REST Framework  
✅ Entendimento de modelos (Models) no Django

---

## 🎯 Objetivos da Aula

Ao final desta aula, o aluno será capaz de:

* Entender o que são relacionamentos entre modelos
* Compreender os diferentes tipos de relacionamentos (ForeignKey, OneToOne, ManyToMany)
* Criar modelos relacionados no Django
* Criar serializers que lidam com relacionamentos
* Criar APIs REST que trabalham com modelos dependentes
* Entender cenários práticos de uso de relacionamentos

---

## 📍 1. Introdução: Por que relacionamentos? (5 min)

### 🧩 O problema real

No mundo real, os dados **não existem isoladamente**. Eles se relacionam entre si:

* Um **Cliente** pode ter vários **Pedidos**
* Um **Pedido** pertence a um **Cliente**
* Um **Produto** pode estar em vários **Pedidos**
* Um **Pedido** pode ter vários **Produtos**
* Um **Usuário** tem um **Perfil** (um para um)

### 💡 Exemplo prático

Imagine um sistema de e-commerce:

```
Cliente (João)
  └── Pedido #1
        ├── Produto: Notebook
        └── Produto: Mouse
  └── Pedido #2
        └── Produto: Teclado
```

**Sem relacionamentos**, teríamos que:
* Repetir dados do cliente em cada pedido
* Manter consistência manualmente
* Correr risco de dados inconsistentes

**Com relacionamentos**, o Django cuida disso para nós! 🎉

---

## 📍 2. Tipos de Relacionamentos no Django (10 min)

O Django oferece **3 tipos principais** de relacionamentos:

| Tipo | Django Field | Descrição | Exemplo |
|------|--------------|-----------|---------|
| **Muitos para Um** | `ForeignKey` | Muitos registros de um modelo pertencem a um registro de outro | Muitos pedidos pertencem a um cliente |
| **Um para Um** | `OneToOneField` | Um registro se relaciona com exatamente um outro registro | Um usuário tem um perfil |
| **Muitos para Muitos** | `ManyToManyField` | Muitos registros se relacionam com muitos outros | Muitos produtos em muitos pedidos |

---

## 📍 3. Relacionamento ForeignKey (Muitos para Um) (15 min)

### 🔹 3.1 O que é ForeignKey?

**ForeignKey** é usado quando **muitos registros** de um modelo pertencem a **um registro** de outro modelo.

### 📊 Exemplo Visual

```
Cliente (João)
  ├── Pedido #1 → Cliente: João
  ├── Pedido #2 → Cliente: João
  └── Pedido #3 → Cliente: João
```

### 💻 Exemplo Prático: Cliente e Pedido

Vamos criar dois modelos onde **Pedido depende de Cliente**:

#### **Passo 1: Criar o modelo Cliente**

```python
# models.py
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
```

#### **Passo 2: Criar o modelo Pedido (com ForeignKey)**

```python
# models.py (continuação)
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
    ]
    
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
```

### 🔍 Explicação dos Parâmetros

* **`Cliente`**: O modelo ao qual este campo se relaciona
* **`on_delete=models.CASCADE`**: Quando um cliente for deletado, todos os seus pedidos também serão deletados
* **`related_name='pedidos'`**: Permite acessar os pedidos de um cliente usando `cliente.pedidos.all()`

### 🔹 3.2 Criar e Aplicar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 🔹 3.3 Criar Serializers com Relacionamento

#### **Serializer do Cliente**

```python
# serializers.py
from rest_framework import serializers
from .models import Cliente, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'data_cadastro']
```

#### **Serializer do Pedido (com relacionamento)**

```python
# serializers.py (continuação)
class PedidoSerializer(serializers.ModelSerializer):
    # Opção 1: Mostrar apenas o ID do cliente
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'data_pedido', 'valor_total', 'status']
```

#### **Serializer do Pedido (mostrando dados do cliente)**

```python
# serializers.py (alternativa)
class PedidoSerializer(serializers.ModelSerializer):
    # Opção 2: Mostrar dados completos do cliente (aninhado)
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.IntegerField(write_only=True)  # Para criar/atualizar
    
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'cliente_id', 'data_pedido', 'valor_total', 'status']
```

### 🔹 3.4 Criar Views

```python
# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Verificar se o cliente existe
        cliente_id = request.data.get('cliente_id') or request.data.get('cliente')
        try:
            cliente = Cliente.objects.get(id=cliente_id)
        except Cliente.DoesNotExist:
            return Response(
                {'erro': 'Cliente não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer.save(cliente=cliente)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### 🔹 3.5 Configurar URLs

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### 🔹 3.6 Testando a API

#### **Criar um Cliente**

```bash
POST /api/clientes/
Content-Type: application/json

{
  "nome": "João Silva",
  "email": "joao@email.com",
  "telefone": "(83) 99999-9999"
}
```

**Resposta:**
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@email.com",
  "telefone": "(83) 99999-9999",
  "data_cadastro": "2025-01-15T10:30:00Z"
}
```

#### **Criar um Pedido para esse Cliente**

```bash
POST /api/pedidos/
Content-Type: application/json

{
  "cliente_id": 1,
  "valor_total": "299.99",
  "status": "pendente"
}
```

**Resposta:**
```json
{
  "id": 1,
  "cliente": {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@email.com",
    "telefone": "(83) 99999-9999",
    "data_cadastro": "2025-01-15T10:30:00Z"
  },
  "data_pedido": "2025-01-15T10:35:00Z",
  "valor_total": "299.99",
  "status": "pendente"
}
```

#### **Listar Pedidos de um Cliente**

```bash
GET /api/clientes/1/pedidos/
```

---

## 📍 4. Relacionamento OneToOne (Um para Um) (10 min)

### 🔹 4.1 O que é OneToOne?

**OneToOne** é usado quando **um registro** se relaciona com **exatamente um outro registro**.

### 📊 Exemplo Visual

```
Usuário (João)
  └── Perfil (um único perfil)
        ├── Bio: "Desenvolvedor Python"
        ├── Foto: "foto.jpg"
        └── Data nascimento: "1990-01-01"
```

### 💻 Exemplo Prático: Usuário e Perfil

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
```

### 🔍 Diferença entre ForeignKey e OneToOne

| ForeignKey | OneToOne |
|------------|----------|
| Um cliente pode ter **muitos** pedidos | Um usuário tem **apenas um** perfil |
| `cliente.pedidos.all()` retorna uma lista | `usuario.perfil` retorna um único objeto |

### 🔹 4.2 Serializer com OneToOne

```python
# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    usuario_email = serializers.EmailField(source='usuario.email', read_only=True)
    
    class Meta:
        model = Perfil
        fields = ['id', 'usuario', 'usuario_username', 'usuario_email', 
                  'bio', 'foto', 'data_nascimento', 'telefone']
```

---

## 📍 5. Relacionamento ManyToMany (Muitos para Muitos) (15 min)

### 🔹 5.1 O que é ManyToMany?

**ManyToMany** é usado quando **muitos registros** de um modelo se relacionam com **muitos registros** de outro modelo.

### 📊 Exemplo Visual

```
Pedido #1
  ├── Produto: Notebook
  ├── Produto: Mouse
  └── Produto: Teclado

Pedido #2
  ├── Produto: Notebook
  └── Produto: Mouse

Produto: Notebook
  ├── Pedido #1
  └── Pedido #2
```

### 💻 Exemplo Prático: Pedido e Produto

#### **Passo 1: Criar modelo Produto**

```python
# models.py
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
```

#### **Passo 2: Atualizar modelo Pedido (adicionar ManyToMany)**

```python
# models.py (atualizar Pedido)
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
    ]
    
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    produtos = models.ManyToManyField(
        Produto,
        through='ItemPedido',  # Tabela intermediária (opcional)
        related_name='pedidos'
    )
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome}"
```

#### **Passo 3: Criar modelo intermediário (opcional, mas recomendado)**

```python
# models.py
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no Pedido #{self.pedido.id}"

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"
        unique_together = ['pedido', 'produto']  # Evita duplicatas
```

### 🔹 5.2 Serializer com ManyToMany

```python
# serializers.py
class ItemPedidoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)
    produto_preco = serializers.DecimalField(source='produto.preco', read_only=True, max_digits=10, decimal_places=2)
    
    class Meta:
        model = ItemPedido
        fields = ['id', 'produto', 'produto_nome', 'produto_preco', 
                  'quantidade', 'preco_unitario']

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.IntegerField(write_only=True)
    itens = ItemPedidoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'cliente_id', 'produtos', 'itens', 
                  'data_pedido', 'valor_total', 'status']
```

### 🔹 5.3 View para criar Pedido com Produtos

```python
# views.py
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Obter dados
        cliente_id = request.data.get('cliente_id')
        produtos_ids = request.data.get('produtos', [])  # Lista de IDs
        itens_data = request.data.get('itens', [])  # Lista com quantidade e preço
        
        # Verificar cliente
        try:
            cliente = Cliente.objects.get(id=cliente_id)
        except Cliente.DoesNotExist:
            return Response(
                {'erro': 'Cliente não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Criar pedido
        pedido = Pedido.objects.create(
            cliente=cliente,
            valor_total=request.data.get('valor_total', 0),
            status=request.data.get('status', 'pendente')
        )
        
        # Adicionar produtos ao pedido
        if itens_data:
            for item_data in itens_data:
                produto_id = item_data.get('produto')
                quantidade = item_data.get('quantidade', 1)
                preco_unitario = item_data.get('preco_unitario')
                
                try:
                    produto = Produto.objects.get(id=produto_id)
                    ItemPedido.objects.create(
                        pedido=pedido,
                        produto=produto,
                        quantidade=quantidade,
                        preco_unitario=preco_unitario or produto.preco
                    )
                except Produto.DoesNotExist:
                    continue
        
        serializer = self.get_serializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

### 🔹 5.4 Testando ManyToMany

```bash
POST /api/pedidos/
Content-Type: application/json

{
  "cliente_id": 1,
  "valor_total": "599.98",
  "status": "pendente",
  "itens": [
    {
      "produto": 1,
      "quantidade": 2,
      "preco_unitario": "299.99"
    },
    {
      "produto": 2,
      "quantidade": 1,
      "preco_unitario": "49.99"
    }
  ]
}
```

---

## 📍 6. Cenários Práticos Comuns (5 min)

### 🔹 Cenário 1: Sistema de Blog

```
Autor (1) ──→ (N) Post
Post (N) ──→ (N) Tag
Post (1) ──→ (1) Categoria
```

### 🔹 Cenário 2: Sistema de E-commerce

```
Cliente (1) ──→ (N) Pedido
Pedido (N) ──→ (N) Produto (via ItemPedido)
Produto (1) ──→ (1) Categoria
```

### 🔹 Cenário 3: Sistema de Rede Social

```
Usuario (1) ──→ (1) Perfil
Usuario (N) ──→ (N) Usuario (amigos - ManyToMany)
Post (1) ──→ (1) Usuario (autor)
Post (N) ──→ (N) Usuario (curtidas - ManyToMany)
```

---

## 📍 7. Boas Práticas e Dicas (5 min)

### ✔️ 1. Sempre defina `related_name`

```python
# Bom
cliente = models.ForeignKey(Cliente, related_name='pedidos')

# Permite: cliente.pedidos.all()
```

### ✔️ 2. Escolha o `on_delete` correto

| Opção | Quando usar |
|-------|-------------|
| `CASCADE` | Se o registro filho não faz sentido sem o pai |
| `PROTECT` | Se não quer permitir deletar o pai enquanto houver filhos |
| `SET_NULL` | Se quer manter os filhos, mas sem referência ao pai |
| `SET_DEFAULT` | Se quer atribuir um valor padrão quando o pai for deletado |

### ✔️ 3. Use tabelas intermediárias para ManyToMany quando necessário

```python
# Quando precisa de campos extras (quantidade, preço, etc.)
produtos = models.ManyToManyField(Produto, through='ItemPedido')
```

### ✔️ 4. Valide relacionamentos no serializer

```python
def validate_cliente_id(self, value):
    if not Cliente.objects.filter(id=value).exists():
        raise serializers.ValidationError("Cliente não encontrado.")
    return value
```

### ✔️ 5. Use `prefetch_related` e `select_related` para otimizar queries

```python
# views.py
queryset = Pedido.objects.select_related('cliente').prefetch_related('produtos')
```

---

## 📍 8. Resumo dos Relacionamentos

| Relacionamento | Campo Django | Quando Usar | Exemplo |
|----------------|--------------|-------------|---------|
| **Muitos para Um** | `ForeignKey` | Muitos registros pertencem a um | Pedidos → Cliente |
| **Um para Um** | `OneToOneField` | Um registro se relaciona com exatamente um | Usuário → Perfil |
| **Muitos para Muitos** | `ManyToManyField` | Muitos registros se relacionam com muitos | Pedidos ↔ Produtos |

---

## 📍 9. Exercício Prático (10 min)

Crie um sistema de **Biblioteca** com os seguintes modelos:

### 🔹 Requisitos:

1. **Autor** (nome, nacionalidade, data_nascimento)
2. **Livro** (título, isbn, ano_publicacao, autor - ForeignKey)
3. **Categoria** (nome, descricao)
4. **LivroCategoria** (livro - ForeignKey, categoria - ForeignKey, ManyToMany implícito)
5. **Emprestimo** (usuario, livro - ForeignKey, data_emprestimo, data_devolucao)

### 🔹 Tarefas:

1. Crie os modelos com os relacionamentos corretos
2. Crie os serializers
3. Crie as views
4. Teste criando:
   - Um autor
   - Um livro desse autor
   - Uma categoria
   - Associar livro à categoria
   - Um empréstimo

---

## 📍 Conclusão

Nesta aula aprendemos:

* ✅ **ForeignKey**: Para relacionamentos "muitos para um"
* ✅ **OneToOneField**: Para relacionamentos "um para um"
* ✅ **ManyToManyField**: Para relacionamentos "muitos para muitos"
* ✅ Como criar serializers que lidam com relacionamentos
* ✅ Como criar APIs REST com modelos dependentes
* ✅ Cenários práticos de uso

### 🎯 Próximos Passos

* Praticar criando diferentes tipos de relacionamentos
* Explorar relacionamentos aninhados (serializers dentro de serializers)
* Aprender sobre otimização de queries com `select_related` e `prefetch_related`
* Estudar sobre paginação e filtros em relacionamentos

---

## 📚 Recursos Adicionais

* [Documentação Django - Relacionamentos](https://docs.djangoproject.com/en/stable/topics/db/models/#relationships)
* [Django REST Framework - Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
* [Django REST Framework - Relations](https://www.django-rest-framework.org/api-guide/relations/)

---

**Bons estudos! 🚀**

