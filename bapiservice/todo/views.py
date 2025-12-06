from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
  queryset = Tarefa.objects.all()
  serializer_class = TarefaSerializer

  