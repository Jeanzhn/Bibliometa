from pessoa import Pessoa

class Membro(Pessoa):
    def __init__(self, id_membro, historico_emprestimos):
        super().__init__(nome, tipo)
        self.id_membro = id_membro
        self.historico_emprestimos = []
    
    def verificar_emprestimo(self):
        if self.historico_emprestimos:
            for emprestimo in self.historico_emprestimos:
                print(f"- {emprestimo['id_emprestimo']} {emprestimo['titulo_livro']} {emprestimo['data_emprestimo']}")
        else:
            emprestimo = "Nenhum empréstimo registrado."
        
    def add_emprestimo(self, id_emprestimo, livro, data_emprestimo):
        emprestimo = {
            'id_emprestimo': id_emprestimo,
            'titulo_livro': livro.titulo,
            'data_emprestimo': data_emprestimo
        }
        self.historico_emprestimos.append(emprestimo)
        