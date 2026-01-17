from datetime import date
from .models import Produto, LogMensagem
from .services import enviar_whatsapp

def verificar_produtos_vencidos():
    print("Verificando produtos vencidos...    executando job")
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