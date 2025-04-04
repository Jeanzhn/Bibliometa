from flask import render_template, request
from main import app

@app.route("/")

def homepage():
    return render_template('base.html')

@app.route("/login")

def login():
    return render_template('bibliometa/login.html')

