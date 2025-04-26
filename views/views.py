from flask import render_template, request
from main import app
from model.livro import buscar_info_livro

@app.route("/")

def homepage():
    return render_template('base.html')

@app.route("/login")

def login():
    return render_template('bibliometa/login.html')

@app.route("/busca_livro", methods=['GET', 'POST'])

def busca_livro():
    if request.method == 'POST':
        parametro = request.form.get('parametro', '')
        resultado_livros = buscar_info_livro(parametro)
        if resultado_livros:
            return render_template('busca_livro.html', resultado_livros=resultado_livros, parametro=parametro)
        else:
            return render_template('busca_livro.html', erro="Nenhum livro encontrado ou erro na busca.")
    return render_template('bibliometa/busca_livro.html')

@app.route("/logout")

def logout():
    return render_template('bibliometa/logout.html')
