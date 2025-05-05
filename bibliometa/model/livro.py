from model.to_json import To_json
import requests

class Livro:
    def __init__(self, titulo, autor, editora, ano, isbn, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.isbn = isbn
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")
                  
    @staticmethod
    def buscar_info_livro(parametro):
        requisicao = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=intitle:{parametro}')
        try:
            newlivro = Livro(
                    titulo = requisicao.json()['items'][0]['volumeInfo']['title'],
                    autor= requisicao.json()['items'][0]['volumeInfo']['authors'][0],
                    editora= requisicao.json()['items'][0]['volumeInfo']['publisher'],
                    ano = requisicao.json()['items'][0]['volumeInfo']['publishedDate'],
                    isbn = requisicao.json()['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'],
                    disponivel= True
                    )
            jalivros = To_json.load_users('data/livros.json')
            for livro in jalivros:
                if newlivro not in jalivros:
                    To_json.save_object(newlivro, 'data/livros.json')
                    return newlivro
                elif newlivro == jalivros[livro]:
                    return jalivros[livro]
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
    
