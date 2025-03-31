from Pessoa import Pessoa
class Autor(Pessoa):
    def __init__(self, nacionalidade, livros):
        super().__init__(nome, idade, tipo)
        self.nacionalidade = nacionalidade
        self.livros = []

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
