# 🏁 **Aula Final – Introdução ao Django (Revisão Completa + Próximos Passos)**

Esta é a aula final da introdução a Django.  
Aqui vamos:

- Reutilizar os aprendizados das aulas anteriores  
- Revisar **todos os conceitos essenciais** que você já viu  
- Deixar uma **apostila completa** para você estudar HTML e CSS  
- Registrar os **principais comandos do Django**  
- Listar tudo que você deve estudar daqui pra frente para evoluir no framework  

*Guarde-a* como MATERIAL DE REFERÊNCIA.

---

# 📘 **Material de Apoio Oficial – HTML e CSS**

Antes de avançar profundamente no Django, é fundamental ter uma boa base em HTML e CSS.  
Aqui está uma excelente apostila para estudar:

👉 **Apostila de HTML e CSS (IFSC)**  
https://docente.ifsc.edu.br/lara.popov/web1/apostila__html_css.pdf  

Use essa apostila como estudo contínuo. Ela complementa tudo mostrado até agora e te prepara para trabalhar com templates no Django.

---

---

# 🧠 **REVISÃO COMPLETA – O QUE VOCÊ APRENDEU ATÉ AQUI**

## 🎯 **1. Conceitos Fundamentais da Web**

### ✔ Cliente e Servidor  
- Cliente → faz requisições (navegador, app)  
- Servidor → processa e devolve respostas  

### ✔ HTTP – O idioma da Web  
- GET → buscar dados  
- POST → enviar dados  
- PUT → atualizar  
- DELETE → remover  

### ✔ Estrutura de uma requisição
- Método (GET, POST…)  
- URL  
- Headers  
- Body  

### ✔ Códigos de resposta
- 200 → OK  
- 404 → Não encontrado  
- 500 → Erro no servidor  
- 302 → Redirecionamento  

---

## 🧱 **2. O que é um Framework**

- Conjunto de ferramentas prontas para acelerar desenvolvimento  
- Ajuda a seguir padrões  
- Evita reescrever tudo do zero  

---

## 🐍 **3. O que é Django**

- Framework web backend escrito em Python  
- Altamente seguro  
- Escalável  
- MVT: Model – View – Template  
- Traz servidor interno, ORM, administração, sistema de templates e mais

---

## 🛠 **4. Instalando e Configurando Django**

### ✔ Criar ambiente virtual

```bash
python -m venv venv
````

### ✔ Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### ✔ Instalar Django:

```bash
pip install django
```

---

## 🚀 **5. Criando o Primeiro Projeto**

### ✔ Criar projeto:

```bash
django-admin startproject meu_projeto
```

ou criar na pasta específica:

```bash
django-admin startproject meu_projeto django-primeiro-app
```

### ✔ Executar o servidor interno

```bash
python manage.py runserver
```

**Por que usar esse comando?**
Porque o Django traz um servidor de desenvolvimento próprio.
Ele atualiza automaticamente sempre que você salva arquivos.

---

## 📂 **6. Estrutura do Projeto Django**

### Arquivos importantes:

* **manage.py** → centro de comando do Django
* **settings.py** → configurações do projeto
* **urls.py** → rotas principais
* **views.py** → funções que processam requisições
* **models.py** → tabelas do banco de dados
* **templates/** → páginas HTML

---

## 🏗 **7. Criando uma Aplicação**

```bash
python manage.py startapp produtos
```

**Por que usar esse comando?**
Porque um projeto é dividido em módulos independentes.
Cada app resolve uma parte do sistema.

Ex.:
`produtos`, `usuarios`, `estoque`, `pedidos`…

### ✔ Registrar app

Em `settings.py`:

```python
INSTALLED_APPS = [
    ...,
    'produtos',
]
```

---

# 🧩 **8. Criando Rotas e Views**

## ✔ Criar uma View:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Django!")
```

## ✔ Criar rota:

No `urls.py` do projeto:

```python
from django.urls import path
from produtos.views import home

urlpatterns = [
    path('', home),
]
```

---

# 📄 **9. Templates (HTML + Django)**

* São arquivos HTML que o Django usa para gerar páginas dinâmicas.
* Ficam normalmente em: `templates/meu_app/*.html`

Exemplo:

```python
return render(request, 'produtos/lista.html', contexto)
```

O Django procura automaticamente na pasta `templates`.

---

# 🗄 **10. Modelos (Models) – O Banco de Dados**

## ✔ Criar modelo:

```python
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
```

### ✔ Criar migração (criar "planta" do banco)

```bash
python manage.py makemigrations
```

**Por que usar esse comando?**
Porque o Django precisa traduzir seus modelos Python em instruções para o banco de dados.

### ✔ Executar migração (criar tabela de verdade)

```bash
python manage.py migrate
```

**Por que usar esse comando?**
Esse comando “constrói” as tabelas no banco com base no modelo criado.

---

# 📝 **11. Criando Formulários**

Exemplo de formulário em HTML:

```html
<form method="POST">
    {% csrf_token %}
    <input type="text" name="nome" placeholder="Nome do produto">
    <input type="number" name="preco" placeholder="Preço">
    <button type="submit">Salvar</button>
</form>
```

Explicação:

* `method="POST"` → envia dados
* `{% csrf_token %}` → segurança obrigatória
* inputs enviam dados para a view

---

# 📦 **12. Salvando dados no banco**

```python
if request.method == "POST":
    nome = request.POST.get("nome")
    preco = request.POST.get("preco")

    Produto.objects.create(nome=nome, preco=preco)
    return redirect("listar_produtos")
```

---

# 📋 **13. Listando Dados**

```python
produtos = Produto.objects.all()
```

Depois enviamos para o template:

```python
return render(request, 'produtos/lista.html', {'produtos': produtos})
```

---

# 🗑 **14. Excluindo Dados**

```python
def excluir_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect("listar_produtos")
```

---

# 🗄 **15. Admin do Django**

Criar usuário admin:

```bash
python manage.py createsuperuser
```

Entrar:

```
http://127.0.0.1:8000/admin
```

Registrar o modelo:

```python
from django.contrib import admin
from .models import Produto

admin.site.register(Produto)
```

---

# 💻 **16. HTML e CSS – Revisão Geral**

HTML → estrutura
CSS → aparência

Exemplo simples de CSS:

```html
<style>
    body {
        background: #f0f0f0;
        font-family: Arial;
    }

    .card {
        padding: 10px;
        margin: 10px;
        background: white;
        border-radius: 8px;
    }
</style>
```

---

---

# ⭐ **SEÇÃO ESPECIAL – TODOS OS PRINCIPAIS COMANDOS DO DJANGO**

## ✔ Criar projeto

```bash
django-admin startproject nome
```

## ✔ Criar app

```bash
python manage.py startapp nome
```

## ✔ Rodar servidor

```bash
python manage.py runserver
```

## ✔ Criar arquivo de migração

```bash
python manage.py makemigrations
```

## ✔ Aplicar migração ao banco

```bash
python manage.py migrate
```

## ✔ Criar usuário administrador

```bash
python manage.py createsuperuser
```

## ✔ Limpar arquivos compilados

```bash
python manage.py collectstatic
```

## ✔ Abrir shell Python com Django carregado

```bash
python manage.py shell
```

---

# 🔮 **O QUE VOCÊ DEVE ESTUDAR A PARTIR DE AGORA (GUIA DE EVOLUÇÃO)**

## 🟦 **1. Templates Avançados**

* Herança de templates
* Inclusão de arquivos
* Filtros e tags do Django

## 🟦 **2. Modelos e Banco de Dados**

* Validators
* Relacionamentos (OneToMany, ManyToMany, OneToOne)
* QuerySet avançado
* Signals do Django

## 🟦 **3. Formulários Avançados**

* Django Forms
* ModelForms
* Validações personalizadas

## 🟦 **4. Autenticação e Autorização**

* Login, logout
* Permissões
* Middleware

## 🟦 **5. Sistema de Arquivos**

* Upload de arquivos
* Upload de imagens

## 🟦 **6. APIs com Django Rest Framework**

* Serializers
* ViewSets
* Rotas automáticas
* JWT e autenticação

## 🟦 **7. Deploy**

* VPS (Ubuntu)
* Configuração de servidor Nginx
* Banco Postgres em produção

## 🟦 **8. Segurança**

* CSRF
* XSS
* SQL Injection
* Proteções automáticas do Django

## 🟦 **9. Boas práticas**

* Organização de apps
* Separação de responsabilidades
* Código limpo

---

# 🎉 **PARABÉNS! VOCÊ FECHOU A MÓDULO DE INTRODUÇÃO AO DJANGO**

Agora você:

✔ Sabe como funciona a web
✔ Entende HTML e CSS básicos
✔ Sabe criar projetos Django
✔ Entende models, views, templates
✔ Sabe cadastrar, listar e excluir dados
✔ Consegue criar rotas
✔ Consegue trabalhar com banco de dados

E está pronto para entrar nos tópicos mais avançados!

Sempre volte a esta apostila, ela é um guia sólido.