import logging
import time

from django.conf import settings
from django.core.management.base import BaseCommand

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from produtos.cron import verificar_produtos_vencidos

logger = logging.getLogger(__name__)


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    Deleta execuções de jobs com mais de 'max_age' segundos.
    Por padrão, mantém apenas os últimos 7 dias (604800 segundos).
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)
    logger.info(f"Execuções de jobs com mais de {max_age} segundos foram deletadas.")


class Command(BaseCommand):
    help = "Executa o APScheduler para processar jobs agendados"

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # Adiciona o job de verificação de produtos vencidos
        scheduler.add_job(
            verificar_produtos_vencidos,
            trigger=CronTrigger(second="*/5"),  # Executa a cada 5 segundos
            id="verificar_produtos_vencidos",
            max_instances=1,
            replace_existing=True,
            name="Verificar produtos vencidos",
        )
        logger.info("Job 'verificar_produtos_vencidos' adicionado.")

        # Adiciona job para limpar execuções antigas
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
        logger.info("Job 'delete_old_job_executions' adicionado.")

        try:
            self.stdout.write(
                self.style.SUCCESS("Iniciando scheduler... (Pressione Ctrl+C para parar)")
            )
            scheduler.start()
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Parando scheduler..."))
            scheduler.shutdown()
            self.stdout.write(self.style.SUCCESS("Scheduler parado com sucesso!"))
