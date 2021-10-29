from tupasys import app
from flask import render_template


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/medidor")
def medidor():
    return render_template('medidor.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

