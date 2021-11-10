from tupasys import app
from flask import render_template

setores = {0: "LP-001", 1: "LP-002", 2: "LP-003", 3: "WAREHOUSE"}

@app.route("/")
def home(): 
    return render_template('home.html', setores=setores)

@app.route("/medidor/")
def medidor():        
    return render_template('medidor.html', setores=setores)

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

