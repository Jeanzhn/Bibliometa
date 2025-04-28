from flask import render_template, request, redirect, url_for, session, jsonify
from model.to_json import To_json
from model.livro import Livro
from main import app
import uuid

@app.route("/")

def homepage():
    return render_template('base.html')

@app.route("/login", methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        nome = request.form.get('nome').lower()
        senha = request.form.get('senha')
        
        users = To_json.load_users('data/users.json')
        
        if nome in users and users[nome]['senha'] == senha:
            session['nome'] = nome
            return redirect(url_for('seabook'))
        else:
            return render_template('bibliometa/login.html', error="Usuário ou senha inválidos")
    
    return render_template('bibliometa/login.html')

@app.route("/register", methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmar_senha = request.form.get('confirmar_senha')
        historico_emprestimo = []
        id_membro = str(uuid.uuid4())
        
        users = To_json.load_users('data/users.json')
        
        if not all([nome, email, senha, confirmar_senha]):
            return "Preencha todos os campos!", 400
        
        if senha != confirmar_senha:
            return "As senhas não coincidem!", 400
        
        if nome in users:
            return render_template('bibliometa/login.html', register_error="Usuário já existe", show_register=True)
        
        if senha in users:
            return render_template('bibliometa/login.html', register_error="Esta senha ja existekkkkkkkkkk foi mal perdi a linha", show_register=True)
        
        session['nome'] = nome
        users[nome] = {'senha': senha, 'email': email, 'id_membro' : id_membro, 'historico_emprestimo': historico_emprestimo}
        To_json.save_object(users, 'data/users.json')
        
        return render_template('bibliometa/seabook.html', )
    
    return render_template('bibliometa/register.html', nome_usuario=session.get('nome'))

@app.route("/seabook", methods=['GET', 'POST'])
 
def seabook():
    if 'nome' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        busca = request.form.get('parametro')
        try:
            resultado_livros = Livro.busca_info_livro(busca)
            if resultado_livros:
                return render_template('bibliometa/seabook.html', livros = [resultado_livros], busca=busca)
            else:
                return render_template('bibliometa/seabook.html', erro="Nenhum livro encontrado ou erro na busca.")
        except Exception as e:
            return render_template('bibliometa/seabook.html', erro=f"Erro ao buscar livros: {e}")
    return render_template('bibliometa/seabook.html', nome_usuario=session.get('nome'))    
 
@app.route("/logout")

def logout():
    session.clear()
    return render_template('bibliometa/logout.html')

@app.route("/forgot")

def forgot():
    return render_template('bibliometa/forgot.html')
