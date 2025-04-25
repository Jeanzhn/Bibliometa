class Pessoa:
    def __init__(self, nome, email, tipo):
        self.nome = nome
        self.email = email
        self.tipo = tipo #membro, admin etc...
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Tipo: {self.tipo}")
    