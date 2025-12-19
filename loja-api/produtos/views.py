from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


"""

list - listar os produtos - GET /produtos/  
create - criar um produto - POST /produtos/ 
retrieve - detalhar um produto - GET /produtos/{id}/
update - atualizar um produto - PUT /produtos/{id}/
partial_update - atualizar parcialmente um produto - PATCH /produtos/{id}/
destroy - deletar um produto - DELETE /produtos/{id}/

"""