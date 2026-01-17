# 🎓 Aula: Integrando Django REST com Gateway de Pagamentos

Bem-vindo(a)! Hoje vamos sair do básico "CRUD" (criar, ler, atualizar, deletar) e entrar no mundo real: **dinheiro**.

Vamos criar um sistema para uma **Associação**. O objetivo é gerar cobranças (Boleto ou PIX) para os associados e, o mais importante, saber automaticamente quando eles pagaram.

### 🗺️ O Cenário

Imagine uma "Associação de Desenvolvedores".

1. Temos os **Associados** (Pessoas).
2. Temos as **Cobranças** (A conta a pagar).
3. Precisamos falar com um **Gateway de Pagamento** (O "banco" digital que processa o PIX/Boleto, como Asaas, Pagar.me, Mercado Pago, etc).

---

## 1. Arquitetura da Solução (O que vamos construir)

Antes de codar, vamos desenhar as rotas (URLs) que sua API precisará.

| Verbo | Rota (Endpoint) | O que faz? |
| --- | --- | --- |
| `POST` | `/api/cobrancas/` | **Gera a cobrança.** Cria no nosso banco e avisa o Gateway para gerar o Boleto/Pix. |
| `GET` | `/api/cobrancas/` | **Consulta.** O frontend usa para mostrar ao associado suas dívidas. |
| `GET` | `/api/cobrancas/{id}/` | **Detalhe.** Mostra o link do boleto ou o Código Pix (Copia e Cola). |
| `POST` | `/api/webhook/` | **A Mágica.** O Gateway acessa essa URL para nos avisar: "O boleto X foi pago!". |

---

## 2. Preparando o Terreno (Models)

Primeiro, precisamos representar nossos dados. Vamos editar o arquivo `models.py`.

Precisamos de duas tabelas: uma para quem paga (`Associado`) e uma para a dívida (`Cobranca`).

```python
# app/models.py
from django.db import models

class Associado(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Cobranca(models.Model):
    TIPO_CHOICES = [
        ('BOLETO', 'Boleto Bancário'),
        ('PIX', 'PIX'),
    ]
    
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('CANCELADO', 'Cancelado'),
    ]

    associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_pagamento = models.CharField(max_length=10, choices=TIPO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    
    # Campos importantes para integração
    id_transacao_gateway = models.CharField(max_length=100, blank=True, null=True) # ID único lá no banco
    link_pagamento = models.URLField(blank=True, null=True) # Link para o boleto
    codigo_pix = models.TextField(blank=True, null=True) # Copia e Cola do Pix

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.associado.nome} - R$ {self.valor} ({self.status})"

```

> **💡 Dica de Ouro:** O campo `id_transacao_gateway` é o vínculo entre o seu sistema e o banco. Sem ele, você não saberá qual boleto foi pago.

---

## 3. A Camada de Integração (Services)

Aqui é onde iniciantes costumam errar: colocar a lógica de falar com o banco externo dentro da `View`. **Não faça isso.** Vamos criar um arquivo separado chamado `services.py`.

Imagine que estamos usando um Gateway fictício. Na vida real, você usaria a biblioteca `requests` para chamar a API do Asaas, Stripe ou MercadoPago.

```python
# app/services.py
import requests
import uuid # Apenas para simular IDs únicos

class GatewayPagamento:
    """
    Classe responsável por falar com o mundo externo (O Banco/Gateway)
    """
    
    API_URL = "https://api.gatewayficticio.com/v1"
    API_KEY = "sua_chave_secreta"

    def gerar_cobranca(self, cliente_nome, valor, tipo):
        """
        Envia os dados para o Gateway e recebe o link/pix de volta.
        """
        # Na vida real, aqui você faria:
        # payload = {'value': valor, 'name': cliente_nome, 'type': tipo}
        # response = requests.post(f"{self.API_URL}/charges", json=payload, headers={...})
        # return response.json()
        
        # SIMULAÇÃO DE RESPOSTA DO GATEWAY:
        print(f"--- CONECTANDO AO GATEWAY: Gerando {tipo} de R${valor} para {cliente_nome} ---")
        
        return {
            "id_transacao": str(uuid.uuid4()), # O banco nos devolve um ID
            "status": "PENDENTE",
            "link_boleto": "https://gateway.com/boleto.pdf" if tipo == 'BOLETO' else None,
            "qrcode_pix": "00020126580014BR.GOV.BCB.PIX..." if tipo == 'PIX' else None
        }

```

---

## 4. Serializers

O Serializer transforma o objeto Python em JSON.

```python
# app/serializers.py
from rest_framework import serializers
from .models import Associado, Cobranca

class AssociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associado
        fields = '__all__'

class CobrancaSerializer(serializers.ModelSerializer):
    # Vamos mostrar os dados do associado junto, para facilitar a leitura
    associado_nome = serializers.CharField(source='associado.nome', read_only=True)

    class Meta:
        model = Cobranca
        fields = ['id', 'associado', 'associado_nome', 'valor', 'tipo_pagamento', 'status', 'link_pagamento', 'codigo_pix']
        read_only_fields = ['status', 'link_pagamento', 'codigo_pix'] # O usuário não pode editar isso manualmente

```

---

## 5. As Views (A Lógica da API)

Agora vamos criar as "tomadas" onde o frontend vai se conectar. Vamos usar `ModelViewSet` para facilitar, mas vamos customizar o momento de **criar** a cobrança.

```python
# app/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Associado, Cobranca
from .serializers import AssociadoSerializer, CobrancaSerializer
from .services import GatewayPagamento # Importamos nosso serviço

class AssociadoViewSet(viewsets.ModelViewSet):
    queryset = Associado.objects.all()
    serializer_class = AssociadoSerializer

class CobrancaViewSet(viewsets.ModelViewSet):
    queryset = Cobranca.objects.all()
    serializer_class = CobrancaSerializer

    def create(self, request, *args, **kwargs):
        """
        Reescrevemos o método CREATE para chamar o Gateway antes de finalizar.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # 1. Salva os dados básicos no nosso banco (ainda sem ID do gateway)
        cobranca = serializer.save(status='PENDENTE')
        
        # 2. Chama o serviço de pagamento
        gateway = GatewayPagamento()
        try:
            resposta_gateway = gateway.gerar_cobranca(
                cliente_nome=cobranca.associado.nome,
                valor=float(cobranca.valor),
                tipo=cobranca.tipo_pagamento
            )
            
            # 3. Atualiza nossa cobrança com os dados que o Gateway devolveu
            cobranca.id_transacao_gateway = resposta_gateway['id_transacao']
            cobranca.link_pagamento = resposta_gateway['link_boleto']
            cobranca.codigo_pix = resposta_gateway['qrcode_pix']
            cobranca.save()
            
            # Retorna os dados atualizados para o usuário ver o boleto/pix
            return Response(CobrancaSerializer(cobranca).data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            # Se der erro no gateway, deletamos a cobrança local para não ficar sujeira
            cobranca.delete()
            return Response({"erro": "Falha ao comunicar com Gateway de Pagamento."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

```

---

## 6. O Webhook: Sabendo se foi pago (Movimentação)

Essa é a parte mais crítica. Como sabemos se o associado pagou o boleto na lotérica? Não vamos ficar perguntando ao banco a cada 5 minutos. **O banco é que nos avisa.**

Isso se chama **Webhook**. É uma rota que deixamos aberta para o Gateway mandar um POST.

Adicione isso no seu `views.py` (ou em um arquivo separado):

```python
from rest_framework.views import APIView

class WebhookPagamentoView(APIView):
    """
    Recebe notificações do Gateway.
    O Gateway vai enviar um JSON tipo: {"id_transacao": "123-abc", "novo_status": "PAGO"}
    """
    def post(self, request):
        dados = request.data
        
        # 1. Pegamos o ID que o gateway mandou
        id_externo = dados.get('id_transacao')
        novo_status_gateway = dados.get('novo_status')
        
        if not id_externo:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
        try:
            # 2. Buscamos a cobrança no nosso banco pelo ID DO GATEWAY
            cobranca = Cobranca.objects.get(id_transacao_gateway=id_externo)
            
            # 3. Atualizamos o status (A tal da "Movimentação")
            if novo_status_gateway == 'PAGO':
                cobranca.status = 'PAGO'
                cobranca.save()
                print(f"💰 SUCESSO! A cobrança {cobranca.id} foi paga!")
                
            elif novo_status_gateway == 'CANCELADO':
                cobranca.status = 'CANCELADO'
                cobranca.save()
                
            return Response({"mensagem": "Recebido com sucesso"}, status=status.HTTP_200_OK)
            
        except Cobranca.DoesNotExist:
            return Response({"erro": "Cobranca não encontrada"}, status=status.HTTP_404_NOT_FOUND)

```

### Configurando as URLs (`urls.py`)

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssociadoViewSet, CobrancaViewSet, WebhookPagamentoView

router = DefaultRouter()
router.register(r'associados', AssociadoViewSet)
router.register(r'cobrancas', CobrancaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/webhook/', WebhookPagamentoView.as_view(), name='webhook'),
]

```

---

## 7. Resumo do Fluxo (Didático)

1. **Requisição:** O Admin do sistema envia um POST para `/api/cobrancas/` dizendo: "O Associado João deve R$ 50,00 no Boleto".
2. **Processamento:** O Django salva "Pendente", chama o `GatewayPagamento`.
3. **Resposta:** O Gateway diz "Ok, toma aqui o link do PDF". O Django salva o link e devolve para o Admin.
4. **Pagamento:** O João paga o boleto no banco dele.
5. **Confirmação (Assíncrona):** No dia seguinte (ou na hora, se for Pix), o Gateway acessa sua URL `/api/webhook/` e diz: "Ei, aquele ID xxxxx foi PAGO".
6. **Atualização:** Seu sistema acha a cobrança e muda o status para `PAGO`.

