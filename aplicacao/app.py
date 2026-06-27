from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


CAMINHO_BD = "sqlite:///banco.db"
BD = SQLAlchemy()
APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = CAMINHO_BD

class Livro(BD.Model):
    __tablename__ = 'livro'
    id = BD.Column(BD.Integer, primary_key=True)
    titulo = BD.Column(BD.String)
    autor = BD.Column(BD.String)
    issn = BD.Column(BD.String)
    data_publicacao = BD.Column(BD.DateTime)
    qtde_paginas = BD.Column(BD.Integer)

    def get_titulo(self):
        return self.titulo

BD.init_app(APP)

with APP.app_context():
    BD.create_all()
    
migrate = Migrate(APP, BD)

@APP.route("/")
def index():
    return render_template('index.html')

@APP.route("/livros", methods=['GET', 'POST'])
def livros():
    livros = Livro.query.all()
    return render_template('livros.html', livros=livros)

if __name__ == '__main__':
    APP.run(debug=True)