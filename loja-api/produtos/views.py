from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # 1. filtro em_estoque=true 
    filterset_fields = ['em_estoque']

    # 2. filtro nome__icontains=nome
    search_fields = ['nome', 'descricao']
 
    ordering_fields = ['preco', 'nome']

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

"""

list - listar os produtos - GET /produtos/  
create - criar um produto - POST /produtos/ 
retrieve - detalhar um produto - GET /produtos/{id}/
update - atualizar um produto - PUT /produtos/{id}/
partial_update - atualizar parcialmente um produto - PATCH /produtos/{id}/
destroy - deletar um produto - DELETE /produtos/{id}/

"""