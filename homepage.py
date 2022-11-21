# INSTALANDO O FLASK - pip install Flask, render_template

# IMPORTANDO O FLASK
from flask import Flask, render_template

# PADRÃO PARA INICIAR O FLASK
app = Flask(__name__)

# CRIAR A 1° PÁGINA DO SITE
'''
TODA PÁGINA POSSUI UM "ROUTE" E "FUNÇÃO"
ROUTE - O CAMINHO/LINK DA PÁGINA
FUNÇÃO - O QUE VOCÊ QUER EXIBIR NA PÁGINA
TEMPLATES - CODIGOS HTML DE CADA PÁGINA'''


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


# COLOCAR O SITE NO AR - SERVER - HEROKU
if __name__ == "__main__":
    app.run(debug=True)
