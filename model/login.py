class login:
    def __init__(self):
        self.admins = {'admin':'0000', 'dono':'0000'}
        self.membros = {'jean':'1234'}

    def verificar_login(self, user, senha):
        if user in self.admins and self.admins[user] == senha:
            return 'Admin'
        elif user in self.membros and self.membros[user] == senha:
            return 'Membro'
        else:
            return None
        
    def cadastrar_user(self, tipo, user, senha):
        if user in self.admins or user in self.membros:
            print("\nEste usuário já existe")
            return False
            
        if tipo.lower() == 'admin':
            self.admins[user] = senha
            print(f"\nAdmin '{user}' cadastrado com sucesso!")
            return True
        elif tipo.lower() == 'membro':
            self.membros[user] = senha
            print(f"\nMembro '{user}' cadastrado com sucesso!")
            return True
        else:
            print("\nUse 'admin' ou 'membro'.")
            return False
        
    def portaria_user(self):
        print('----- Sistema Biblimet Login -----')
        user = input('Usuário:').strip()
        senha = input('Senha:').strip()
        on_off = False
        
        tipo_user = self.verificar_login(user, senha)
        
        while not on_off:
            if tipo_user == 'Admin':
                print(f'Bem vindo {tipo_user}:{user} você que manda')
                on_off = True
            elif tipo_user == 'Membro':
                print(f'Boa leitura {tipo_user}:{user}')
                on_off = True
            else:
                print('Você não tem um login')
        login = self.new_user(tipo_user, user, senha)
        
    def new_user(self, tipo_user, user, senha):
        print("\n---- Novo Desbravador na área ----")
        
        while True:
            tipo_user = input('Tipo de Usuario(admin/membro)').capitalize()#sim, um membro pode criar um user admin para ele pq sim
            if tipo_user not in ['Admin', 'Membro']:
                print("Tipo inválido! Digite 'admin' ou 'membro'.")
                continue
        
            user = input("Nome de usuário: ").strip()
            senha = input("Senha: ").strip()
            confirma_senha = input("Confirme a senha: ").strip()
            
            if senha != confirma_senha:
                print("\nErro: As senhas não coincidem!")
                continue
                
            if self.new_user(tipo_user, user, senha):
                self.membros[user] = senha
                break
            
if __name__ == '__main__':
    sistema = login()
    
    resultado = sistema.portaria_user()
    