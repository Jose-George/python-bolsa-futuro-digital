# 🧪 **Aula: Boas Práticas de Desenvolvimento de Software e Clean Code com Django REST**

**Duração:** 1h
**Nível:** Iniciante → Intermediário
**Tecnologias:** Python, Django, Django REST Framework

---

## 🎯 **Objetivos da Aula**

Ao final desta aula, o aluno será capaz de:

* Entender o que são boas práticas de desenvolvimento de software
* Aplicar conceitos de **Clean Code** em Python
* Organizar um projeto Django REST de forma profissional
* Criar APIs mais limpas, legíveis e sustentáveis
* Melhorar nomes, funções, classes e responsabilidades
* Estruturar pastas, modularizar e escrever código reutilizável

---

# 📍 **1. Introdução (5 min)**

### Por que escrever código limpo?

* Facilita manutenção
* Reduz bugs
* Facilita colaboração
* Permite escalar o projeto
* Aumenta produtividade

### O mantra:

> **"Código é lido muito mais vezes do que é escrito."**

---

# 📍 **2. Conceitos Fundamentais de Clean Code (10 min)**

### ✔️ Nomes claros e descritivos

* Funções com nomes verbais: `get_user`, `calculate_total`
* Classes com substantivos: `OrderService`, `NotificationHandler`
* Variáveis que explicam o que guardam: `total_price`, `is_active`

### ✔️ Funções pequenas e com uma única responsabilidade

❌ Má prática:

```python
def process_user(data):
    # cria, valida, envia email e loga
```

✔️ Boa prática:

```python
def create_user(data):
def validate_user(data):
def send_welcome_email(user):
def log_user_creation(user):
```

---

# 📍 **3. Boas Práticas em Python (10 min)**

### ✔️ PEP8 como base

* 4 espaços
* Linhas ≤ 79 caracteres
* Funções separadas por 2 linhas
* Imports organizados

### ✔️ Imports organizados

Ordem correta:

1. **Imports nativos do Python**
2. **Imports de terceiros**
3. **Imports do projeto**

```python
import os
from datetime import datetime

from rest_framework import serializers

from core.models import User
```

### ✔️ Tipagem opcional (typing)

```python
def soma(a: int, b: int) -> int:
    return a + b
```

---

# 📍 **4. Clean Code aplicado ao Django REST (15 min)**

## 🔹 4.1 Estrutura recomendada de projeto

```
project/
│
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── services.py
│   │   └── repositories.py
│   ├── products/
│   └── orders/
│
├── core/
│   ├── settings.py
│   └── utils.py
```

### Por quê?

* Facilita manutenção
* Várias equipes podem atuar separadamente
* Evita arquivos gigantes

---

## 🔹 4.2 Views limpas (usando ViewSets)

### ❌ Controller gordo

```python
class UserViewSet(ModelViewSet):
    def create(self, request):
        data = request.data
        user = User.objects.create(**data)
        send_email(user.email)
        logger.info(f"User {user.id} created")
        return Response(UserSerializer(user).data)
```

### ✔️ Controller magro + camada de serviço

```python
# services.py
def create_user_service(data):
    user = User.objects.create(**data)
    send_welcome_email(user)
    log_user_creation(user)
    return user

# views.py
class UserViewSet(ModelViewSet):
    def create(self, request):
        user = create_user_service(request.data)
        return Response(UserSerializer(user).data)
```

---

## 🔹 4.3 Serializers limpos

### ✔️ Validadores bem organizados

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Email inválido.")
        return value
```

---

## 🔹 4.4 Modelos pequenos e coesos

### ❌ Anti-padrão: modelo gigante

```python
class User(models.Model):
    name = models.CharField(...)
    email = models.EmailField(...)
    cpf = models.CharField(...)
    address = models.CharField(...)
    phone = models.CharField(...)
    # dezenas de campos irrelevantes juntos
```

### ✔️ Dividir para organizar

Criar entidades menores:

* `User`
* `UserProfile`
* `UserAddress`

---

# 📍 **5. Boas práticas essenciais para APIs (10 min)**

### ✔️ URLs significativas

* `/users/`
* `/users/<id>/orders/`

Evitar:

* `/getAllUsers`
* `/doUserStuff`

---

## ✔️ Status Codes corretos

| Ação              | Código  |
| ----------------- | ------- |
| Criado            | **201** |
| Sucesso           | **200** |
| Sem conteúdo      | **204** |
| Erro de validação | **400** |
| Não autorizado    | **401** |
| Proibido          | **403** |
| Não encontrado    | **404** |

---

## ✔️ Padronize respostas

### Bom:

```json
{
  "data": { ... },
  "message": "Usuário criado com sucesso."
}
```

### Evite:

```json
{"ok": "yes", "obj": "..."}
```

---

# 📍 **6. Arquitetura e Separação de Responsabilidades (5 min)**

### Camadas recomendadas:

* **View** → recebe requisição
* **Serializer** → valida dados
* **Service** → regra de negócio
* **Repository** → abstrai o ORM (opcional)
* **Model** → representa o domínio

### Benefícios:

* Código testável
* Menos acoplamento
* Facilita mudanças

---

# 📍 **7. Checklist de Clean Code para Django REST (5 min)**

### ✔️ Antes de entregar uma feature, verifique:

* [ ] Funções pequenas
* [ ] Nomes claros
* [ ] Views magras
* [ ] Regras de negócio fora das views
* [ ] Serializers organizados
* [ ] Models sem gordura
* [ ] Comentários apenas quando necessário
* [ ] Arquitetura coerente
* [ ] Tratamento de erros correto
* [ ] Respostas padronizadas

---

# 📍 **8. Exercício Prático (10 min)**

Crie um app chamado `clientes` com:

### 🔹 1. Modelo

`Cliente` com:

* nome
* email
* telefone

### 🔹 2. Serializer

Com validação de email.

### 🔹 3. Service

Função:

```python
create_cliente_service(data)
```

### 🔹 4. ViewSet magro

Chamando apenas o service.

### 🔹 5. URLs limpas

`/clientes/`

### 🎯 Objetivo:

Aplicar **todas** as boas práticas aprendidas.

---

# 📍 **Conclusão**

Ao aplicar **Clean Code + boas práticas + arquitetura por camadas**, seu projeto:

* Cresce sem virar uma bagunça
* Facilita pull requests
* Reduz bugs
* Fica mais profissional

