from pessoa import Pessoa
class Autor(Pessoa):
    def __init__(self, nacionalidade, livros):
<<<<<<< HEAD
        super().__init__(nome)
        self.nacionalidade = nacionalidade
        self.livros = []
    
=======
        super().__init__(nome, idade, tipo)
        self.nacionalidade = nacionalidade
        self.livros = []

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Livros:{self.livros}")
        
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
