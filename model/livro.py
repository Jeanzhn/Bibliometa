class Livro:
    def __init__(self, titulo, autor, editora, ano, isbn, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.isbn = isbn
        self.disponivel = True
    
    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")
        print(f"Ano: {self.ano}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponível: {'Sim' if self.disponivel else 'Não'}")

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")
            