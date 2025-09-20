
class Autor: 
    def __init__(self, nome, nacionalidade):
       self.__nome = nome
       self.__nacionalidade = nacionalidade

    def get_nome(self):
        return self.__nome  
    
    def get_nacionalidade(self):
        return self.__nacionalidade
    
    def set_nacionalidade(self, nova_nacionalidade):
        self.__nacionalidade = nova_nacionalidade
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome 


  
class Livro:
    def __init__(self, titulo, autor: Autor):
        self.__titulo = titulo
        self.__autor = autor  
      
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor 
    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor 

autor01 = Autor("George Orwell", "Inglês")
autor02 = Autor("J.K. Rowling", "Inglês")

livro01 = Livro("1984", autor01)
livro02 = Livro("Harry Potter e a Pedra Filosofal", autor02)
livro03 = Livro("Harry Potter e a Câmara Secreta", autor02)

print(f"O livro {livro01.get_titulo()} foi escrito por {livro01.get_autor().get_nome()}, que é {livro01.get_autor().get_nacionalidade()}.")