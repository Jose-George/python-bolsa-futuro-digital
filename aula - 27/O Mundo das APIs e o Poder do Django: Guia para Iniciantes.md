# 🚀 O Mundo das APIs e o Poder do Django: Guia para Iniciantes

Se você está começando a programar, provavelmente já ouviu a sigla **API**. Ela é a cola que mantém a internet unida. Além disso, no mundo Python, você ouvirá muito sobre **ORM**.

Este documento vai te explicar esses conceitos, mostrar a diferença de programar com e sem ORM, e te guiar passo a passo na criação de uma API.

-----

## 1\. O Que é uma API? (A Analogia do Restaurante)

**API** significa *Application Programming Interface*.

Imagine um restaurante:

1.  **Você (O Cliente):** Quer comer (precisa de dados).
2.  **A Cozinha (O Banco de Dados):** Tem os ingredientes e prepara o prato.
3.  **O Garçom (A API):** Você não entra na cozinha para pegar comida. Você pede ao garçom, ele vai à cozinha e traz o prato.

**A API é o garçom.** Ela recebe pedidos, busca os dados no servidor e devolve a resposta.

-----

## 2\. O Que é ORM? 

Antes de colocarmos a mão na massa, precisamos entender o **ORM** (Object-Relational Mapping).

Bancos de dados falam uma língua chamada **SQL** (tabelas, linhas, colunas).
O Python fala uma língua de **Objetos** (classes, atributos, métodos).

O **ORM** é um tradutor automático. Ele permite que você mexa no banco de dados usando apenas código Python, sem precisar escrever SQL manualmente.

### Comparativo: Com ORM vs. Sem ORM

Imagine que queremos buscar **todas as tarefas não concluídas** no banco de dados.

#### ❌ O jeito difícil (Sem ORM - Usando SQL Puro)

Sem ORM, você precisa conectar manualmente, escrever a query em texto e converter o resultado na mão. É trabalhoso e perigoso.

```python
import sqlite3

# 1. Conectar ao banco
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()

# 2. Escrever SQL manualmente (se errar uma letra, quebra)
sql = "SELECT * FROM tarefas WHERE concluida = 0;"
cursor.execute(sql)

# 3. Pegar os dados brutos (vem como uma lista de tuplas, ex: [(1, 'Estudar'), ...])
dados_brutos = cursor.fetchall()

# 4. Converter na mão para usar no Python
lista_tarefas = []
for linha in dados_brutos:
    tarefa = {'id': linha[0], 'titulo': linha[1], 'concluida': linha[2]}
    lista_tarefas.append(tarefa)

conexao.close()
```

#### ✅ O jeito Django (Com ORM)

Com o ORM do Django, você trata a tabela do banco como se fosse uma classe Python normal.

```python
# Uma linha simples, limpa e legível
tarefas_pendentes = Tarefa.objects.filter(concluida=False)
```

### Por que usar ORM? (Benefícios)

1.  **Segurança:** O ORM protege automaticamente contra *SQL Injection* (um tipo comum de ataque hacker).
2.  **Agilidade:** Você escreve 90% menos código para fazer a mesma coisa.
3.  **Flexibilidade:** Se hoje você usa um banco simples (SQLite) e amanhã quer mudar para um banco gigante (PostgreSQL), você **não precisa mudar nenhuma linha de código**. O ORM se adapta sozinho.

-----

## 3\. Prática: Criando a API com Django REST Framework

Vamos criar um sistema de **Tarefas (To-Do List)**.

### Passo 1: Inicializando o Projeto

Abra seu terminal (CMD ou PowerShell) e digite os comandos abaixo, um por um:

```bash
# 1. Cria a pasta do projeto principal chamada 'config'
django-admin startproject config .

# 2. Cria o aplicativo específico de tarefas
python manage.py startapp todo

# 3. (Opcional) Tente rodar o servidor para ver se funcionou até aqui
python manage.py runserver
# Se aparecer um foguete ou página de sucesso no navegador, pare o servidor (Ctrl+C) e continue.
```

### Passo 2: Configurando os Apps

Agora vá no seu editor de código. No arquivo `config/settings.py`, precisamos avisar ao Django que instalamos o `rest_framework` e criamos o app `todo`.

```python
# config/settings.py

INSTALLED_APPS = [
    ...
    'rest_framework', # Adicione esta linha
    'todo',           # Adicione esta linha
]
```

### Passo 3: Criando o Modelo (Usando o ORM)

No arquivo `todo/models.py`, vamos definir a estrutura da nossa tabela.

```python
# todo/models.py
from django.db import models

class Tarefa(models.Model):
    # O ORM vai transformar isso em colunas no banco de dados automaticamente
    titulo = models.CharField(max_length=100)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
```

### Passo 4: Criando o Banco de Dados

Sempre que mexemos no `models.py`, precisamos rodar dois comandos no terminal para atualizar o banco de dados real.

```bash
# 1. Cria o arquivo de instruções (Cria a "planta" da casa)
python manage.py makemigrations

# 2. Executa as instruções no banco (Constrói a casa)
python manage.py migrate
```

### Passo 5: O Serializer e a View

Agora vamos criar a "cola" que transforma os dados do banco (ORM) em JSON para a API.

Crie um arquivo novo chamado `serializers.py` dentro da pasta `todo`:

```python
# todo/serializers.py
from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__' # Pega todos os campos do modelo
```

Agora edite o arquivo `todo/views.py`:

```python
# todo/views.py
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    # Aqui o ORM busca todos os objetos
    queryset = Tarefa.objects.all() 
    serializer_class = TarefaSerializer
```

### Passo 6: As Rotas (URLs)

Precisamos criar o endereço para acessar a API. Edite o arquivo `config/urls.py`:

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TarefaViewSet

# Cria as rotas automáticas para GET, POST, PUT, DELETE
router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Nossos endpoints ficarão em /api/tarefas/
]
```

### Passo 7: Rodando a API

Volte ao terminal e inicie o servidor:

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/api/tarefas/` no seu navegador. Você verá uma interface pronta para adicionar e listar tarefas\!

-----

## 4\. Consumindo a API no Front-end

O Front-end não sabe o que é Python, Django ou ORM. Ele só entende **JSON**. Veja como consumir os dados que criamos acima.

```javascript
const url = 'http://127.0.0.1:8000/api/tarefas/';

// Função Assíncrona (Async/Await)
async function pegarTarefas() {
    try {
        // O fetch vai bater na porta do servidor
        const resposta = await fetch(url);
        
        // Converte a resposta texto para objeto JavaScript (JSON)
        const dados = await resposta.json();
        
        console.log("Tarefas carregadas:", dados);
        
        // Exemplo de como usar os dados na tela
        dados.forEach(tarefa => {
            document.body.innerHTML += `<p>${tarefa.titulo} - ${tarefa.concluida ? 'OK' : 'Pendente'}</p>`
        });

    } catch (erro) {
        console.error("Deu erro:", erro);
    }
}

pegarTarefas();
```

-----

## Resumo dos Comandos Importantes

| Comando | O que faz? |
| :--- | :--- |
| `django-admin startproject` | Cria a estrutura inicial de pastas. |
| `python manage.py startapp` | Cria um "módulo" novo (ex: clientes, produtos, tarefas). |
| `python manage.py makemigrations` | Lê seu código Python e cria um script de alteração para o banco. |
| `python manage.py migrate` | Aplica as alterações no banco de dados real. |
| `python manage.py runserver` | Liga o servidor local para você testar. |

