from flask import render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
from model.to_json import To_json
from model.livro import Livro
from main import app
import uuid
import logging
import sys
import re

# Cria um handler para o console (StreamHandler)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)  # Define o nível mínimo de log para este handler

# Cria um formatter para o log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Adiciona o handler ao logger da aplicação Flask
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)  # Define o nível mínimo de log para o logger da aplicação


@app.route("/")
def homepage():
    app.logger.info("passando pela Home")
    """Renderiza a página inicial da aplicação."""
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome')
        app.logger.debug(f"Nome do forms:{nome}")
        senha = request.form.get('senha')
        
        users = To_json.load_users('data/users.json')
        admin = To_json.load_users('data/admin.json')
        
        if nome in users and users[nome]['senha'] == senha:
            session['nome'] = nome
            return redirect(url_for('seabook', tipoUser=users[nome]['tipo']))
        elif nome in admin and admin[nome]['senha'] == senha:
            session['nome'] = nome
            return redirect(url_for('seabook', tipoUser=admin[nome]['tipo']))
        else:
            return render_template('bibliometa/login.html', error="Usuário ou senha inválidos")
    
    return render_template('bibliometa/login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Handles user registration.

    If the request method is POST, it validates the submitted form data,
    checks for existing users, saves the new user to the database,
    and redirects the user to the login page.

    If the request method is GET, it renders the registration form.
    """
    if request.method == 'POST':
        try:
          nome = request.form.get('nome')
          app.logger.debug("Nome do forms:",nome)
          email = request.form.get('email')
          app.logger.debug("Email do forms:",email)
          senha = request.form.get('senha')
          app.logger.debug("Senha do forms:",senha) 
          confirmar_senha = request.form.get('confirmar_senha')
          app.logger.debug("Confirmar senha do forms:",confirmar_senha)
          typeUser = "user"
          historico_emprestimo = []
          id_membro = str(uuid.uuid4())
        except Exception as e:
          return render_template('bibliometa/login.html', register_error= f"Erro ao processar o formulário:{e}" , show_register=True)
        new_user = To_json.load_users('data/users.json')
        
        if len(senha)>12 or len(senha)<4:
            return "Senha deve ter no minimo 4 caracteres e máximo 12 caracteres", 400

        if not all([nome, email, senha, confirmar_senha]):
            return "Preencha todos os campos!", 400
            
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            return "Email invalido", 400
            
        if senha != confirmar_senha:
            return "As senhas não coincidem!", 400

        if nome in new_user:
            return render_template('bibliometa/login.html', register_error="Usuário já existe", show_register=True)

        new_user[nome] = {
            'senha': senha,
            'email': email,
            'id_membro': id_membro,
            'historico_emprestimos': historico_emprestimo,
            'tipo': typeUser
        }

        To_json.save_users(new_user, 'data/users.json')
        
        session['nome']=nome
        # Redireciona para a página de login com uma mensagem de sucesso
        return redirect(url_for('login', registration_success=True))

    # Renderiza o formulário de registro para requisições GET
    return render_template('bibliometa/register.html')

@app.route("/seabook", methods=['GET', 'POST'])
def seabook(): 
    if 'nome' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        busca = request.form.get('parametro')
        try:
            resultado_livros = Livro.buscar_info_livro(busca)
            if resultado_livros:
                return render_template('bibliometa/seabook.html', livros = [resultado_livros], busca=busca) 
            else:
                return render_template('bibliometa/seabook.html', erro="Nenhum livro encontrado ou erro na busca.")
        except Exception as e:
            return render_template('bibliometa/seabook.html', erro=f"Erro ao buscar livros: {e}")
    return render_template('bibliometa/seabook.html', nome_usuario=session.get('nome'), tipoUser=request.args.get('tipoUser'))    
 
@app.route("/logout")

def logout():
    session.clear()
    return render_template('bibliometa/logout.html')

@app.route("/forgot")

def forgot():
    return render_template('bibliometa/forgot.html')

@app.route("/lists" , methods=['GET', 'POST'])
def lists():
    listarUsers = To_json.load_users('data/users.json')
    listarBook = To_json.load_users('data/livros.json')
    return render_template('bibliometa/lists.html', listarBooks=listarBook, listarUsers=listarUsers)
