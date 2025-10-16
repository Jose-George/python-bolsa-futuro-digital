
class Livro: 
  
  def __init__(self, titulo, autor, ano):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.disponivel = True
    self.emprestado_para = None
  
  def emprestar(self, usuario_id: int) -> bool:
    if self.disponivel:
      self.disponivel = False
      self.emprestado_para = usuario_id
      return True
    return False
  
  def devolver(self) -> bool:
      self.disponivel = True
      self.emprestado_para = None
  
  