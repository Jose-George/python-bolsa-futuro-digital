from Livro import Livro

class Biblioteca: 

  def __init__(self):
    self.usuarios = []
    self.livros = []

  def cadastrar_livro(self, titulo: str, autor: str, ano: int) -> Livro:
    livro = Livro(titulo, autor, ano)
    self.livros.append(livro)
    return livro