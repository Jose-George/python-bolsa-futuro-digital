from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        # Validação básica
        if nome and preco:
            try:
                # Converte o preço de string para Decimal
                preco_decimal = Decimal(preco)
                Produto.objects.create(nome=nome, preco=preco_decimal)
                return redirect('listar_produtos')
            except (ValueError, TypeError):
                # Se houver erro na conversão, retorna o formulário com erro
                return render(request, 'produtos/form.html', {
                    'erro': 'Preço inválido. Use um número válido (ex: 10.50)'
                })
        else:
            return render(request, 'produtos/form.html', {
                'erro': 'Por favor, preencha todos os campos.'
            })

    return render(request, 'produtos/form.html')

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')

        # Validação básica
        if nome and preco:
            try:
                # Converte o preço de string para Decimal
                preco_decimal = Decimal(preco)
                produto.nome = nome
                produto.preco = preco_decimal
                produto.save()
                return redirect('listar_produtos')
            except (ValueError, TypeError):
                # Se houver erro na conversão, retorna o formulário com erro
                return render(request, 'produtos/form.html', {
                    'produto': produto,
                    'erro': 'Preço inválido. Use um número válido (ex: 10.50)',
                    'editar': True
                })
        else:
            return render(request, 'produtos/form.html', {
                'produto': produto,
                'erro': 'Por favor, preencha todos os campos.',
                'editar': True
            })

    return render(request, 'produtos/form.html', {'produto': produto, 'editar': True})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')
