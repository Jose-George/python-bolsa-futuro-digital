from django.shortcuts import render, redirect
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        Produto.objects.create(nome=nome, preco=preco)
        return redirect('listar_produtos')

    return render(request, 'produtos/form.html')

def excluir_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('listar_produtos')
