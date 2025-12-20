# Aula 31: Segurança e Autenticação em APIs

Bem-vindo à Aula 31! Hoje não vamos apenas digitar códigos; vamos entender **como** uma API se protege.

Muitas vezes, criamos APIs que funcionam perfeitamente no nosso computador, mas que, se colocadas na internet, permitiriam que qualquer pessoa apagasse todo o banco de dados. Vamos resolver isso.

## 1. Entendendo o Problema (Teoria)

### 1.1. O que é "Estado" (State)?
Você já notou que, quando você entra no Facebook ou Instagram, você não precisa digitar sua senha a cada clique que dá? Isso acontece porque o site mantém uma **Sessão** ativa. O servidor "lembra" de você.

Em **APIs REST**, as coisas funcionam de forma diferente. Elas devem ser **Stateless** (Sem Estado).

> **O que significa Stateless?**
> Significa que o servidor **não lembra** da requisição anterior.
>
> Imagine que você vai a um clube exclusivo.
> - **Com Estado (Sessão):** O porteiro decora seu rosto. Você entra e sai quando quiser.
> - **Sem Estado (API REST):** O porteiro tem amnésia. Toda vez que você passar pela porta, você precisa mostrar sua carteirinha. **TODA VEZ.**

### 1.2. Autenticação vs Autorização
São duas palavras parecidas, mas com funções vitais diferentes:

1.  **Autenticação (Quem é você?):**
    - É o ato de verificar sua identidade.
    - Ex: Mostrar seu RG, digitar Login/Senha.
    - *Resultado:* "Ok, você é o João."

2.  **Autorização (O que você pode fazer?):**
    - É o ato de verificar suas permissões.
    - Ex: O João pode entrar na piscina? O João pode entrar na sala da diretoria?
    - *Resultado:* "João pode ver os dados, mas não pode apagar nada."

---

## 2. Na Prática: O "Crachá" da API (Token)

Como a API é "esquecida" (stateless), não podemos pedir login e senha a cada clique. Isso seria inseguro e chato (ter que enviar a senha via rede toda hora).

A solução é o **Token**.
1.  Você envia Login/Senha **uma vez**.
2.  A API responde com um código longo e único (o Token). Ex: `9054f7aa...`
3.  Nas próximas requisições, você só mostra esse código. Ele é seu **Crachá**.

Vamos implementar isso no Django agora.

---

## 3. Implementando no Django

Vamos usar o projeto `loja` da aula anterior.

### Passo 1: Instalar o Porteiro (App de Auth)

O Django Restricted Framework já vem com um sistema de Tokens pronto. Só precisamos ativá-lo.

Abra `loja/settings.py` e adicione `rest_framework.authtoken` aos apps instalados:

```python
# loja/settings.py

INSTALLED_APPS = [
    # ... outros apps ...
    'rest_framework',
    'rest_framework.authtoken',  # <--- ADICIONE ESTA LINHA
    'produtos',
]
```

### Passo 2: Criar as Tabelas

O sistema de tokens precisa de uma tabela no banco de dados para guardar quem é dono de qual token.

Execute no terminal:

```bash
python manage.py migrate
```

### Passo 3: Configurar a Segurança

Agora precisamos dizer ao DRF: *"Olha, a partir de agora, use Tokens para identificar as pessoas, e só deixe entrar quem estiver autenticado."*

Ainda no `loja/settings.py`, adicione (ou edite) a configuração do `REST_FRAMEWORK`:

```python
# loja/settings.py

REST_FRAMEWORK = {
    # 1. Autenticação (Como eu te identifico?)
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    
    # 2. Permissão (O que você pode fazer?)
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', # Apenas autenticados entram!
    ],
}
```

> **CUIDADO:** Com essa configuração `IsAuthenticated`, **TODAS** as rotas da sua API agora estão bloqueadas para o público. É segurança máxima.

---

## 4. Testando (E vendo falhar)

Vamos ver o bloqueio funcionando.

1.  Rode o servidor: `python manage.py runserver`
2.  Tente acessar `http://127.0.0.1:8000/api/produtos/` no navegador ou Postman.

**Resultado Esperado:**
```json
{
    "detail": "As credenciais de autenticação não foram fornecidas."
}
```
**Status:** `401 Unauthorized`

Isso é ótimo! Nossa API está segura. Ninguém entra sem crachá.

---

## 5. Entrando com o Crachá (Token)

Para entrar, precisamos de um Token.

### 5.1. Gerar um Token (Jeito Rápido)

Como ainda não criamos uma tela de login, vamos gerar um token via terminal para o nosso superusuário (que criamos na aula passada).

No terminal (com o servidor parado ou em outra aba):

```bash
# Substitua 'admin' pelo nome do seu usuário
python manage.py drf_create_token admin
```

Ele vai devolver algo assim: `Token: 9054f7aa82...1234`

**Copie esse código.** Esse é seu crachá.

### 5.2. Usando o Token

Vá no **Postman** (ou Insomnia):

1.  Coloque a URL: `GET http://127.0.0.1:8000/api/produtos/`
2.  Vá na aba **Headers** (Cabeçalhos).
3.  Adicione uma nova linha:
    - **Key:** `Authorization`
    - **Value:** `Token 9054f7aa82...1234` (O código que você copiou, com a palavra "Token " e um espaço antes).
4.  Clique em Send.

**Resultado:** A lista de produtos aparece! 🎉

---

## 6. Exercício Prático: Agenda Segura

Vamos criar algo novo para praticar. Imagine um sistema de contatos pessoais. Só você pode ver seus contatos.

**O Desafio:**

1.  Crie um novo app chamado `agenda`. (`python manage.py startapp agenda`)
2.  Adicione `agenda` no `settings.py`.
3.  Crie um Modelo simples em `agenda/models.py`:
    ```python
    class Contato(models.Model):
        nome = models.CharField(max_length=100)
        telefone = models.CharField(max_length=20)
        
        def __str__(self):
            return self.nome
    ```
4.  Rode as migrações (`makemigrations` e `migrate`).
5.  Crie o `Serializer` e o `ViewSet` para esse Contato (lembra como faz?).
6.  Registre a rota `/contatos` no `urls.py`.

**O Teste Final:**
- Tente acessar `/api/contatos/` sem o Header de Authorization. (Deve falhar)
- Tente acessar COM o Header de Authorization. (Deve funcionar)

---

### Dica de Ouro:
Se você quiser que uma rota específica seja pública (ex: Cadastro de Usuário), você pode sobrescrever a permissão apenas naquela View:

```python
class MinhaViewPublica(viewsets.ModelViewSet):
    permission_classes = [] # Lista vazia = sem restrição
    # ...
```

---

**Resumo da Aula:**
- APIs são **Stateless** (não têm memória de sessão).
- Precisamos enviar o **Token** (Crachá) em **toda** requisição.
- Autenticação = Identidade. Autorização = Permissão.
- O Django faz o trabalho pesado com `IsAuthenticated` e `TokenAuthentication`.
