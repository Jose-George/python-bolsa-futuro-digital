from datetime import datetime
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from .cron import verificar_produtos_vencidos

logger = logging.getLogger(__name__)


def start():
    """
    Inicializa e configura o scheduler do APScheduler.
    Esta função é chamada automaticamente quando o Django inicia (via apps.py).
    """
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Registra o job de verificação de produtos vencidos
    # Executa a cada minuto (equivalente ao '* * * * *' do crontab)
    scheduler.add_job(
        verificar_produtos_vencidos,
        trigger=CronTrigger(minute="*"),  # Executa a cada minuto
        id="verificar_produtos_vencidos",  # ID único para o job
        max_instances=1,  # Apenas uma instância por vez
        replace_existing=True,  # Substitui job existente se já estiver registrado
        name="Verificar produtos vencidos",
    )
    logger.info("Job 'verificar_produtos_vencidos' adicionado ao scheduler.")

    # Adiciona job para limpar execuções antigas (mantém apenas últimas 7 dias)
    scheduler.add_job(
        delete_old_job_executions,
        trigger=CronTrigger(
            day_of_week="mon", hour="00", minute="00"
        ),  # Toda segunda-feira à meia-noite
        id="delete_old_job_executions",
        max_instances=1,
        replace_existing=True,
        name="Limpar execuções antigas de jobs",
    )
    logger.info("Job 'delete_old_job_executions' adicionado ao scheduler.")

    try:
        logger.info("Iniciando scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Parando scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler parado com sucesso!")


def delete_old_job_executions(max_age=604_800):
    """
    Deleta execuções de jobs com mais de 'max_age' segundos.
    Por padrão, mantém apenas os últimos 7 dias (604800 segundos).
    
    Esta função ajuda a manter o banco de dados limpo, removendo
    registros antigos de execuções de jobs.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)
    logger.info(f"Execuções de jobs com mais de {max_age} segundos foram deletadas.")
