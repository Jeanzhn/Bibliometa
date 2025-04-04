import json

with open('data/users.json', 'r') as file:
    table_users = json.load(file)

def login(nome_user, senha_user):
    for nome, senha in table_users['membros']:
        if nome_user not in table_users['nome'] and senha_user not in table_users['senha']:
            return False
            