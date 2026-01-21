# Migração de django-crontab para django-apscheduler

## 📋 Sumário Executivo

Este documento detalha a migração do sistema de agendamento de tarefas do projeto **estoquecronjob** de `django-crontab` para `django-apscheduler`. A migração foi realizada para melhorar a integração com o Django, facilitar o gerenciamento de jobs e proporcionar maior controle sobre a execução de tarefas agendadas.

---

## 🔄 Mudanças Realizadas

### 1. Configuração do Projeto (`settings.py`)

**Arquivo:** [`estoquecronjob/settings.py`]

#### Removido:
```python
INSTALLED_APPS = [
    # ...
    'django_crontab',
]

CRONJOBS = [
    ('* * * * *', 'produtos.cron.verificar_produtos_vencidos'),
]
```

#### Adicionado:
```python
INSTALLED_APPS = [
    # ...
    'django_apscheduler',
]

# APScheduler Configuration
SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    'apscheduler.executors.processpool': {
        "type": "threadpool"
    },
}

SCHEDULER_AUTOSTART = True
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
```

### 2. Novo Arquivo de Scheduler

**Arquivo:** [`produtos/scheduler.py`] **(NOVO)**

Este arquivo centraliza a configuração do APScheduler:

- **Função `start()`**: Inicializa o scheduler em background
- **Job principal**: `verificar_produtos_vencidos` - executa a cada minuto
- **Job de manutenção**: `delete_old_job_executions` - limpa registros antigos toda segunda-feira à meia-noite
- **Configurações**: Timezone, jobstore (banco de dados), e prevenção de duplicação de jobs

### 3. Melhorias na Função de Verificação

**Arquivo:** [`produtos/cron.py`]

#### Melhorias implementadas:

- **Decorator `@util.close_old_connections`**: Previne problemas com conexões de banco de dados em long-running processes
- **Logging estruturado**: Substituiu `print()` por `logger.info()` e `logger.error()`
- **Verificação otimizada**: Adiciona log quando não há produtos vencidos
- **Contagem de produtos**: Informa quantos produtos vencidos foram encontrados
- **Tratamento de erros**: Log detalhado de falhas no envio de mensagens

### 4. Management Command

**Arquivo:** [`produtos/management/commands/runscheduler.py`] **(NOVO)**

Command Django para executar o scheduler:

```bash
python manage.py runscheduler
```

**Características:**
- Usa `BlockingScheduler` para manter o processo rodando
- Registra os mesmos jobs do `scheduler.py`
- Tratamento gracioso de interrupção (Ctrl+C)
- Feedback visual no console

### 5. Estrutura de Diretórios Criada

```
produtos/
├── management/
│   ├── __init__.py          (NOVO)
│   └── commands/
│       ├── __init__.py      (NOVO)
│       └── runscheduler.py  (NOVO)
├── scheduler.py             (NOVO)
├── cron.py                  (MODIFICADO)
└── apps.py                  (MODIFICADO)
```

---

## 💡 Motivos da Substituição

### Limitações do django-crontab

1. **Dependência do sistema operacional**: Requer acesso ao crontab do sistema
2. **Difícil debug**: Erros são difíceis de rastrear
3. **Sem histórico**: Não mantém registro de execuções
4. **Configuração externa**: Jobs ficam fora do controle do Django
5. **Problemas em produção**: Requer configuração manual do cron em cada servidor

### Vantagens do django-apscheduler

1. **✅ Integração nativa com Django**: Jobs são gerenciados pelo ORM
2. **✅ Histórico de execuções**: Tabela `DjangoJobExecution` armazena todas as execuções
3. **✅ Melhor logging**: Integração com sistema de logging do Django
4. **✅ Gerenciamento via Admin**: Possibilidade de visualizar jobs no Django Admin
5. **✅ Flexibilidade**: Suporta diversos tipos de triggers (cron, interval, date)
6. **✅ Controle de concorrência**: `max_instances` previne execuções simultâneas
7. **✅ Portabilidade**: Funciona em qualquer ambiente sem depender do cron do SO

---

## ⚙️ Como Configurar e Manter os Schedulers

### Instalação de Dependências

#### 1. Instalar o django-apscheduler

O `django-apscheduler` é um wrapper do APScheduler para Django que permite agendar tarefas periódicas de forma integrada ao framework.

**Instalação via pip:**

```bash
pip install django-apscheduler
```

**Instalação de versão específica (recomendado para produção):**

```bash
pip install django-apscheduler==0.6.2
```

**Atualizar o requirements.txt:**

Adicione a dependência ao arquivo `requirements.txt` do projeto:

```txt
django-apscheduler==0.6.2
```

**Dependências instaladas automaticamente:**

O `django-apscheduler` instalará automaticamente suas dependências:
- `apscheduler>=3.0.0` - O scheduler principal
- `pytz` - Para gerenciamento de timezones
- `tzlocal` - Para detecção automática do timezone local

**Verificar instalação:**

```bash
pip show django-apscheduler
```

Saída esperada:
```
Name: django-apscheduler
Version: 0.6.2
Summary: APScheduler for Django
Home-page: https://github.com/jcass77/django-apscheduler
Author: Jarek Glowacki
License: MIT
Requires: apscheduler, Django, pytz, tzlocal
```

**Verificar compatibilidade com Django:**

O `django-apscheduler` é compatível com:
- Django 2.2+
- Python 3.6+

Verifique sua versão do Django:

```bash
python -c "import django; print(django.get_version())"
```

#### 2. Desinstalar django-crontab (opcional)

Se você ainda tem o `django-crontab` instalado, remova-o após confirmar que a migração está funcionando:

```bash
pip uninstall django-crontab
```

**Remover do requirements.txt:**

Remova a linha `django-crontab` do arquivo `requirements.txt`.

### Configuração Inicial

1. **Executar migrações:**

```bash
python manage.py migrate
```

Isso criará as tabelas necessárias:
- `django_apscheduler_djangojob`
- `django_apscheduler_djangojobexecution`

### Executando o Scheduler

#### Em Desenvolvimento

Execute o management command:

```bash
python manage.py runscheduler
```

O scheduler ficará rodando e você verá logs no console:

```
Iniciando scheduler... (Pressione Ctrl+C para parar)
Job 'verificar_produtos_vencidos' adicionado.
Job 'delete_old_job_executions' adicionado.
Iniciando verificação de produtos vencidos...
Nenhum produto vencido encontrado.
```

#### Em Produção

Para manter o scheduler rodando continuamente em produção, você precisa de um **supervisor de processos**. Aqui estão as opções mais comuns:

##### Opção 1: systemd (Linux)

Crie um arquivo `/etc/systemd/system/django-scheduler.service`:

```ini
[Unit]
Description=Django APScheduler
After=network.target

[Service]
Type=simple
User=seu-usuario
WorkingDirectory=/caminho/para/estoquecronjob
Environment="PATH=/caminho/para/venv/bin"
ExecStart=/caminho/para/venv/bin/python manage.py runscheduler
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Ative e inicie o serviço:

```bash
sudo systemctl enable django-scheduler
sudo systemctl start django-scheduler
sudo systemctl status django-scheduler
```

##### Opção 2: Supervisor

Instale o supervisor:

```bash
sudo apt-get install supervisor
```

Crie `/etc/supervisor/conf.d/django-scheduler.conf`:

```ini
[program:django-scheduler]
command=/caminho/para/venv/bin/python manage.py runscheduler
directory=/caminho/para/estoquecronjob
user=seu-usuario
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/var/log/django-scheduler.log
```

Recarregue o supervisor:

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start django-scheduler
```

##### Opção 3: Docker

Se estiver usando Docker, adicione um serviço no `docker-compose.yml`:

```yaml
services:
  scheduler:
    build: .
    command: python manage.py runscheduler
    depends_on:
      - db
    restart: always
```

### Adicionando Novos Jobs

Para adicionar um novo job agendado:

1. **Crie a função** em `produtos/cron.py`:

```python
@util.close_old_connections
def meu_novo_job():
    logger.info("Executando meu novo job...")
    # Sua lógica aqui
```

2. **Registre o job** em `produtos/management/commands/runscheduler.py`:

```python
scheduler.add_job(
    meu_novo_job,
    trigger=CronTrigger(hour="*/2"),  # A cada 2 horas
    id="meu_novo_job",
    max_instances=1,
    replace_existing=True,
    name="Meu Novo Job",
)
```

3. **Reinicie o scheduler**

### Monitoramento

#### Via Logs

Os logs são automaticamente gerados. Configure o logging no `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'scheduler.log',
        },
    },
    'loggers': {
        'produtos.cron': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
```

#### Via Django Admin

Você pode visualizar as execuções dos jobs no Django Admin:

1. Registre os models em `produtos/admin.py`:

```python
from django.contrib import admin
from django_apscheduler.models import DjangoJob, DjangoJobExecution

admin.site.register(DjangoJob)
admin.site.register(DjangoJobExecution)
```

2. Acesse `/admin/` e navegue até "Django Apscheduler"

#### Via Banco de Dados

Consulte diretamente as tabelas:

```sql
-- Ver jobs registrados
SELECT * FROM django_apscheduler_djangojob;

-- Ver histórico de execuções
SELECT * FROM django_apscheduler_djangojobexecution 
ORDER BY run_time DESC 
LIMIT 10;
```

---

## ⚠️ Impactos e Cuidados na Migração

### Impactos Principais

#### 1. **Mudança de Arquitetura**

| Aspecto | django-crontab | django-apscheduler |
|---------|----------------|-------------------|
| **Execução** | Cron do sistema operacional | Processo Django contínuo |
| **Gerenciamento** | `crontab add/remove` | Management command |
| **Persistência** | Arquivo crontab | Banco de dados |
| **Logs** | Arquivo separado ou syslog | Sistema de logging do Django |

#### 2. **Requisito de Processo Contínuo**

> [!WARNING]
> O `django-apscheduler` requer um processo Django rodando continuamente. Se o processo parar, os jobs não serão executados.

**Antes (django-crontab):**
- Jobs executavam mesmo com Django desligado
- Gerenciado pelo cron do sistema

**Depois (django-apscheduler):**
- Requer `python manage.py runscheduler` rodando
- Necessita supervisor em produção

#### 3. **Consumo de Recursos**

- **Memória**: Processo Django adicional rodando
- **Conexões de banco**: Mantém conexão ativa
- **CPU**: Mínimo, apenas durante execução dos jobs

### Cuidados Importantes

#### ✅ **1. Remover Jobs Antigos do Crontab**

Antes de migrar, remova os jobs do django-crontab:

```bash
python manage.py crontab remove
```

Verifique se foram removidos:

```bash
crontab -l
```

#### ✅ **2. Evitar Duplicação de Schedulers**

> [!CAUTION]
> Nunca execute múltiplas instâncias do `runscheduler` simultaneamente, pois isso causará execução duplicada de jobs.

**Solução**: Use `max_instances=1` em cada job (já configurado)

#### ✅ **3. Gerenciar Conexões de Banco de Dados**

Sempre use o decorator `@util.close_old_connections` em funções de job:

```python
@util.close_old_connections
def minha_funcao():
    # código aqui
```

Isso previne o erro: `MySQL server has gone away`

#### ✅ **4. Timezone**

Certifique-se de que `TIME_ZONE` está configurado corretamente em `settings.py`:

```python
TIME_ZONE = 'America/Sao_Paulo'  # Ajuste conforme necessário
USE_TZ = True
```

#### ✅ **5. Limpeza de Execuções Antigas**

O job `delete_old_job_executions` já está configurado para limpar registros antigos. Isso previne crescimento excessivo da tabela `DjangoJobExecution`.

#### ✅ **6. Tratamento de Erros**

Jobs que falham não param o scheduler. Configure logging adequado para monitorar falhas:

```python
try:
    # código do job
except Exception as e:
    logger.error(f"Erro no job: {e}", exc_info=True)
```

#### ✅ **7. Testes**

Teste os jobs manualmente antes de colocar em produção:

```python
# No shell do Django
python manage.py shell

>>> from produtos.cron import verificar_produtos_vencidos
>>> verificar_produtos_vencidos()
```

### Checklist de Migração

- [x] Atualizar `settings.py`
- [x] Criar `scheduler.py`
- [x] Atualizar `cron.py` com logging
- [x] Criar management command `runscheduler`
- [ ] Instalar `django-apscheduler`: `pip install django-apscheduler`
- [ ] Executar migrações: `python manage.py migrate`
- [ ] Remover jobs antigos: `python manage.py crontab remove` (se ainda instalado)
- [ ] Testar localmente: `python manage.py runscheduler`
- [ ] Configurar supervisor em produção
- [ ] Monitorar logs após deploy

---

## 🔍 Troubleshooting

### Problema: "No module named 'django_apscheduler'"

**Solução:**
```bash
pip install django-apscheduler
```

### Problema: Jobs não executam

**Verificações:**
1. O comando `runscheduler` está rodando?
2. Há erros nos logs?
3. As migrações foram executadas?
4. O timezone está correto?

### Problema: "MySQL server has gone away"

**Solução:** Certifique-se de usar `@util.close_old_connections` em todas as funções de job.

### Problema: Jobs executam em duplicata

**Solução:** 
- Verifique se há apenas uma instância do `runscheduler` rodando
- Confirme que `max_instances=1` está configurado
- Use `replace_existing=True` ao adicionar jobs

---

## 📚 Referências

- [Documentação django-apscheduler](https://github.com/jcass77/django-apscheduler)
- [Documentação APScheduler](https://apscheduler.readthedocs.io/)
- [Django Management Commands](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)

---

## 📝 Conclusão

A migração de `django-crontab` para `django-apscheduler` proporciona:

- ✅ Melhor integração com Django
- ✅ Histórico completo de execuções
- ✅ Logging estruturado
- ✅ Maior controle e flexibilidade
- ✅ Facilidade de manutenção

**Próximos passos:**
1. Instalar dependências
2. Executar migrações
3. Testar localmente
4. Configurar supervisor em produção
5. Monitorar execuções

Para dúvidas ou problemas, consulte a seção de Troubleshooting ou a documentação oficial.
