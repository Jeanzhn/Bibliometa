from pessoa import Pessoa

class Membro(Pessoa):
    def __init__(self, id_membro, historico_emprestimos):
        super().__init__(nome, idade, tipo)
        self.id_membro = id_membro
        self.historico_emprestimos = []
    
    def verificar_emprestimo(self):
        if self.historico_emprestimos:
            for emprestimo in self.historico_emprestimos:
                print(f"- {emprestimo['titulo_livro']} ({emprestimo['data_emprestimo']})")
        else:
            emprestimo = "Nenhum empréstimo registrado."
    
    def exibir_informacoes_membro(self):
        print(f"Nome: {self.nome}")
        print(f"ID do Membro: {self.id_membro}")
        print(f"Histórico de Empréstimos:{self.emprestimo}")
        
    def add_emprestimo(self, livro, data_emprestimo):
        emprestimo = {
            'titulo_livro': livro.titulo,
            'data_emprestimo': data_emprestimo
        }
        self.historico_emprestimos.append(emprestimo)
    
    def exibir_informacoes_membro(self):
        print(f"Nome: {self.nome}")
        print(f"ID do Membro: {self.id_membro}")
        print(f"Histórico de Empréstimos:{self.emprestimo}")
        
 