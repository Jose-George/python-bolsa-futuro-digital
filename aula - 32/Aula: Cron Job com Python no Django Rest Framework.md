# 🕒 Aula: Cron Job com Python no Django Rest Framework

### Verificando validade de produtos e enviando alertas via WhatsApp (simulado)

---

## 🎯 Objetivo da Aula

Ao final desta aula, o aluno será capaz de:

* Entender **o que é um Cron Job**
* Criar um **projeto Django com Django Rest Framework**
* Criar **models**, **APIs** e **tarefas automáticas**
* Criar um **cron job** que:

  * Verifica produtos vencidos
  * Envia uma mensagem (simulada) via WhatsApp
  * Salva logs das mensagens enviadas
* Criar uma **API para consultar os logs de mensagens**

---

## 🧠 Público-alvo

* Iniciantes em **Python**
* Iniciantes em **Django / Django Rest Framework**
* Alunos que **nunca ouviram falar de Cron Job**

---

## 📌 Pré-requisitos

* Python 3.10+
* Conhecimento básico de Python (variáveis, funções)
* Terminal / Prompt de comando

---

## 🧩 Parte 1 — O que é um Cron Job?

### ❓ O que significa "Cron Job"?

Um **Cron Job** é uma **tarefa automática** que roda em um horário definido.

📌 Exemplos do dia a dia:

* Verificar todo dia às **08h** se um produto venceu
* Enviar relatórios toda **segunda-feira**
* Apagar arquivos antigos automaticamente

💡 Pense assim:

> "Quero que meu sistema execute algo **sozinho**, sem alguém clicar em um botão."

---

## 🧩 Parte 2 — Criando o Projeto Django

### 2.1 Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

### 2.2 Instalar dependências

```bash
pip install django djangorestframework django-crontab
```

📌 **O que cada coisa faz?**

* `django` → framework web
* `djangorestframework` → criar APIs
* `django-crontab` → criar cron jobs dentro do Django

---

### 2.3 Criar o projeto

```bash
django-admin startproject estoque
cd estoque
python manage.py startapp produtos
```

---

### 2.4 Registrar apps no `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_crontab',
    'produtos',
]
```

---

## 🧩 Parte 3 — Criando os Models (Banco de Dados)

### ❓ O que é um Model?

Um **Model** representa uma **tabela no banco de dados**.

---

### 3.1 Model Produto

```python
# produtos/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    data_validade = models.DateField()

    def __str__(self):
        return self.nome
```

📌 Esse model cria uma tabela chamada **Produto** com:

* Nome do produto
* Data de validade

---

### 3.2 Model LogMensagem

```python
class LogMensagem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem enviada para {self.produto.nome}"
```

📌 Esse model guarda:

* Qual produto gerou a mensagem
* Qual mensagem foi enviada
* Data e hora do envio

---

### 3.3 Criar o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧩 Parte 4 — Simulando uma API do WhatsApp

⚠️ **Importante**: Não vamos usar WhatsApp real.
Vamos **simular** uma API.

---

### 4.1 Criar serviço de WhatsApp

```python
# produtos/services.py
def enviar_whatsapp(numero, mensagem):
    print("📲 Enviando WhatsApp...")
    print(f"Para: {numero}")
    print(f"Mensagem: {mensagem}")
    return True
```

💡 Isso simula uma API externa.

---

## 🧩 Parte 5 — Criando o Cron Job

### 5.1 Criar arquivo de tarefas

```python
# produtos/cron.py
from datetime import date
from .models import Produto, LogMensagem
from .services import enviar_whatsapp

def verificar_produtos_vencidos():
    hoje = date.today()
    produtos = Produto.objects.filter(data_validade__lte=hoje)

    for produto in produtos:
        mensagem = f"O produto {produto.nome} está vencido desde {produto.data_validade}"

        enviado = enviar_whatsapp(
            numero="+5583900000000",
            mensagem=mensagem
        )

        if enviado:
            LogMensagem.objects.create(
                produto=produto,
                mensagem=mensagem
            )
```

📌 O que esse código faz?

1. Pega a data de hoje
2. Busca produtos vencidos
3. Envia mensagem
4. Salva o log no banco

---

## 🧩 Parte 6 — Configurando o Cron Job

### 6.1 Registrar no `settings.py`

```python
CRONJOBS = [
    ('0 8 * * *', 'produtos.cron.verificar_produtos_vencidos'),
]
```

📌 Significado:

* `0 8 * * *` → Todo dia às **08:00**
* Função que será executada automaticamente

---

### 6.2 Ativar o cron

```bash
python manage.py crontab add
```

📌 Para listar:

```bash
python manage.py crontab show
```

---

## 🧩 Parte 7 — Criando a API de Logs (Django REST)

### 7.1 Serializer

```python
# produtos/serializers.py
from rest_framework import serializers
from .models import LogMensagem

class LogMensagemSerializer(serializers.ModelSerializer):
    produto = serializers.StringRelatedField()

    class Meta:
        model = LogMensagem
        fields = '__all__'
```

---

### 7.2 View

```python
# produtos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LogMensagem
from .serializers import LogMensagemSerializer

class LogMensagemView(APIView):
    def get(self, request):
        logs = LogMensagem.objects.all()
        serializer = LogMensagemSerializer(logs, many=True)
        return Response(serializer.data)
```

---

### 7.3 URL

```python
# produtos/urls.py
from django.urls import path
from .views import LogMensagemView

urlpatterns = [
    path('logs/', LogMensagemView.as_view()),
]
```

```python
# estoque/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('produtos.urls')),
]
```

---

## 🧩 Parte 8 — Testando a Aplicação

### 🔎 Acessar os logs

```http
GET http://localhost:8000/api/logs/
```

📌 Resposta esperada:

```json
[
  {
    "id": 1,
    "produto": "Leite Integral",
    "mensagem": "O produto Leite Integral está vencido desde 2026-01-10",
    "data_envio": "2026-01-17T08:00:00"
  }
]
```

---

## ✅ Conclusão

🎉 Parabéns!
Você aprendeu:

* O que é um **Cron Job**
* Como criar **tarefas automáticas no Django**
* Como integrar com **APIs externas (simuladas)**
* Como salvar **logs no banco**
* Como criar uma **API REST**

---

## 🚀 Próximos Passos (Sugestões)

* Enviar mensagem apenas **uma vez por produto**
* Criar campo `notificado = True`
* Criar painel admin
* Usar **Celery + Redis**
* Integrar com WhatsApp real (Twilio, Z-API)

