import json
with open('dados.json', 'r') as file:
    dados = json.load(file)

def login(nome, senha):
    for nome_usuario, senha_usuario in dados['pessoas']:
        if nome_usuario not in dados['nome'] and senha_usuario not in dados['senha']:
            
