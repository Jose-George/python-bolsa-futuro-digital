class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumo(self):
        return f"{self.titulo} por {self.autor} — {self.paginas} páginas"

    def __repr__(self):
        return f"Livro(titulo={self.titulo!r}, autor={self.autor!r}, paginas={self.paginas})"