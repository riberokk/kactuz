from symtable import Class

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from kactuz.models import Users

class FormLogin(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	senha = PasswordField("Senha", validators=[DataRequired()])
	botao = SubmitField("Entrar")

class FormCadastro(FlaskForm):
	usuario = StringField("Usuario", validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
	confirma_senha = PasswordField("Senha", validators=[DataRequired(), EqualTo("senha", message="As senhas não coincidem.")])
	botao = SubmitField("Cadastrar")
	def validate_email(self, email):
		usuario = Users.query.filter_by(email=email.data).first()
		if usuario:
			return ValidationError("E-mail ja cadastrado, faça login para continuar")

class FormCompra(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	cep = StringField("CEP", validators=[DataRequired()])
	address = StringField("Endereço", validators=[DataRequired()])
	numero = IntegerField("Numero", validators=[DataRequired()])
	complemento = StringField("Complemento")
	botao = SubmitField("Comprar")

class FormTamanho(FlaskForm):
	tamanho = SelectField("Escolha o Tamanho", choices=[('P'), ('M'), ('G'), ('GG')], validators=[DataRequired()])
	botao = SubmitField("Comprar")
