from rest_framework.decorators import api_view
from rest_framework.response import Response

# Banco de dados em memória
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 49.90},
    {"id": 2, "nome": "Tênis", "preco": 199.90},
]

@api_view(["GET"])
def listar_produtos(request):
    return Response(produtos)

@api_view(["POST"])
def criar_produto(request):
    novo = request.data
    novo["id"] = len(produtos) + 1
    produtos.append(novo)
    return Response(novo, status=201)