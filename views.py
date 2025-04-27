from flask import render_template, request, redirect, url_for, session, jsonify
from model import to_json 
from main import app

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
        senha = request.form.get('senha')
        confirm_senha = request.form.get('confirm_senha')
        
        users = to_json.load_users()
        
        if not nome or not senha:
            return render_template('login.html', register_error="Todos os campos são obrigatórios", show_register=True)
        
        if senha != confirm_senha:
            return render_template('login.html', register_error="As senhas não coincidem", show_register=True)
        
        if nome in users:
            return render_template('login.html', register_error="Usuário já existe", show_register=True)
        
        users[nome] = {'senha': senha}
        to_json.save_users(users)
        
        return render_template('login.html', success="Registro realizado com sucesso! Faça login.")
    
    return redirect(url_for('login'))

@app.route("/busca_livro", methods=['GET', 'POST'])

def busca_livro():
    if 'nome' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        parametro = request.form.get('parametro', '')
        resultado_livros = busca_livro(parametro)
        if resultado_livros:
            return render_template('busca_livro.html', resultado_livros=resultado_livros, parametro=parametro)
        else:
            return render_template('busca_livro.html', erro="Nenhum livro encontrado ou erro na busca.")
    return render_template('bibliometa/busca_livro.html')

@app.route("/logout")

def logout():
    return render_template('bibliometa/logout.html')
