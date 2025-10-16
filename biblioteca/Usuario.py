
class Usuario: 
  def __init__(self, nome: str, id: int):
    self.nome = nome
    self.id = id
    self.livros_emprestados = []
  
  def adicionar_livro(self, livro_titulo: str):
    self.livros_emprestados.append(livro_titulo)

  def remover_livro(self, livro_titulo: str):
    if livro_titulo in self.livros_emprestados:
      self.livros_emprestados.remove(livro_titulo)
      
      
