
from rest_framework import serializers
from .models import LogMensagem

class LogMensagemSerializer(serializers.ModelSerializer):
    produto = serializers.StringRelatedField()

    class Meta:
        model = LogMensagem
        fields = '__all__'