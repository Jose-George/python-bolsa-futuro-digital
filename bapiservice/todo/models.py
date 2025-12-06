from django.db import models

class Tarefa(models.Model):
    # O ORM vai transformar isso em colunas no banco de dados automaticamente
    titulo = models.CharField(max_length=100)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo



