from flask import render_template, request, redirect, url_for, session, jsonify
from model import to_json
from main import app
import uuid

@app.route("/")

def homepage():
    return render_template('base.html')

@app.route("/login", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        
        users = to_json.load_users()
        
        if nome in users and users[nome]['senha'] == senha:
            session['nome'] = nome
            return redirect(url_for('busca_livro'))
        else:
            return render_template('login.html', error="Usuário ou senha inválidos")
    
    return render_template('bibliometa/login.html')

@app.route("/register", methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmar_senha = request.form.get('confirmar_senha')
        id_membro = str(uuid.uuid4())
        
        users = to_json('users.json')
        
        if not all([nome, email, senha, confirmar_senha]):
            return "Preencha todos os campos!", 400
        
        if senha != confirmar_senha:
            return "As senhas não coincidem!", 400
        
        if nome in users:
            return render_template('login.html', register_error="Usuário já existe", show_register=True)
        
        if senha in users:
            return render_template('login.html', register_error="Esta senha ja existe", show_registrer=True)
        
        users[nome] = {'senha': senha, 'email': email, 'id_membro' : id_membro}
        users.to_json('user.json')
        
        return render_template('seabook.html', success="Registro realizado com sucesso! Bem vindo.")
   
    return render_template('bibliometa/register.html')

@app.route("/seabook", methods=['GET', 'POST'])
 
def busca_livro():
    return render_template('bibliometa/seabook.html')
    #if 'nome' not in session:
        #return redirect(url_for('login'))
    if request.method == 'POST':
        parametro = request.form.get('parametro', '')
        resultado_livros = busca_livro(parametro)
        if resultado_livros:
            return render_template('seabook.html', resultado_livros=resultado_livros, parametro=parametro)
        else:
            return render_template('seabook.html', erro="Nenhum livro encontrado ou erro na busca.")
        
    
 
@app.route("/logout")

def logout():
    return render_template('bibliometa/logout.html')

@app.route("/forgot")

def forgot():
    return render_template('bibliometa/forgot.html')
