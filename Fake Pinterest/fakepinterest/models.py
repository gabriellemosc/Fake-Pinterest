#CRIAR A ESTRUTURA DO BANCO DE DADOS
from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin


class Usuario(database.Model, UserMixin):
    __tablename__ = 'usuario'  # Defina o nome da tabela explicitamente
    
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False, unique=True)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))