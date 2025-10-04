class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco):
        self.itens.append((nome, preco))

    def total(self):
        return sum(preco for _, preco in self.itens)

def test_carrinho_de_compras():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Livro", 50)
    carrinho.adicionar_item("Mouse", 100)
    assert carrinho.total() == 150
