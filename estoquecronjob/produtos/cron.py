from datetime import date
import logging

from .models import Produto, LogMensagem
from .services import enviar_whatsapp

logger = logging.getLogger(__name__)


def verificar_produtos_vencidos():
    """
    Verifica produtos vencidos e envia notificação via WhatsApp.
    Executado automaticamente pelo APScheduler a cada minuto.
    """
    logger.info("Iniciando verificação de produtos vencidos...")
    hoje = date.today()
    produtos = Produto.objects.filter(data_validade__lte=hoje)

    if not produtos.exists():
        logger.info("Nenhum produto vencido encontrado.")
        return

    logger.info(f"Encontrados {produtos.count()} produto(s) vencido(s).")

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
            logger.info(f"Mensagem enviada para produto: {produto.nome}")
        else:
            logger.error(f"Falha ao enviar mensagem para produto: {produto.nome}")

    logger.info("Verificação de produtos vencidos concluída.")