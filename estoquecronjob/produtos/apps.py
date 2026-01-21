from django.apps import AppConfig


class ProdutosConfig(AppConfig):
    name = 'produtos'

    def ready(self):
        """
        Inicializa o scheduler quando o Django inicia.
        Nota: Este método é chamado apenas quando usando runscheduler command.
        """
        pass  # O scheduler será iniciado via management command

