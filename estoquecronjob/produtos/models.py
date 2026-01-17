from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    data_validade = models.DateField()

    def __str__(self):
        return self.nome

class LogMensagem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem enviada para {self.produto.nome}"