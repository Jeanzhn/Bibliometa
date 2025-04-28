<<<<<<< HEAD
from model.to_json import To_json
=======
from to_json import To_json
import json
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
import requests

class Livro:
    def __init__(self, titulo, autor, editora, ano, isbn, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.isbn = isbn
<<<<<<< HEAD
        self.disponivel = disponivel
=======
        self.disponivel = True
    
    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")
        print(f"Ano: {self.ano}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponível: {'Sim' if self.disponivel else 'Não'}")
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")
<<<<<<< HEAD
            
    @staticmethod
    def buscar_info_livro(parametro):
        requisicao = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=intitle:{parametro}')
        try:
            livro = Livro(
                    titulo = requisicao.json()['items'][0]['volumeInfo']['title'],
                    autor= requisicao.json()['items'][0]['volumeInfo']['authors'][0],
                    editora= requisicao.json()['items'][0]['volumeInfo']['publisher'],
                    ano = requisicao.json()['items'][0]['volumeInfo']['publishedDate'],
                    isbn = requisicao.json()['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'],
                    disponivel= True
                    )
            To_json.save_object(livro, 'data/livros.json')
            return livro
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
    
=======

    def buscar_info_livro(parametro):
        requisicao = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={parametro}')
        try:
            new_livro={
                "livros":[
                    {
                    'titulo': requisicao.json()['items'][0]['volumeInfo']['title'],
                    'autor': requisicao.json()['items'][0]['volumeInfo']['authors'][0],
                    'editora': requisicao.json()['items'][0]['volumeInfo']['publisher'],
                    'ano': requisicao.json()['items'][0]['volumeInfo']['publishedDate'],
                    'isbn': requisicao.json()['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'],
                    'disponivel': True
                    }
                ]
            }
            with open("data/livros.json", "w" , encoding='utf-8') as file:
                json.dump(new_livro, file, indent=4, ensure_ascii=False)
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None  
>>>>>>> 1e2e812574405ef881ee2d99d2c854746fd86e9c
