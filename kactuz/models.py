from kactuz import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Users.query.get(int(id_usuario))

class Users(database.Model, UserMixin):
	id = database.Column(database.Integer, primary_key=True)
	usuario = database.Column(database.String, nullable=False, unique=True)
	email = database.Column(database.String, nullable=False, unique=True)
	senha = database.Column(database.String, nullable=False)
      
class Address(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    endereco = database.Column(database.String, nullable=False)
    numero = database.Column(database.Integer, nullable=False)
    complemento = database.Column(database.String, nullable=True)
    cep = database.Column(database.String, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
    
class Purchase(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    tamanho = database.Column(database.String, nullable=False)
    id_usuario = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
     