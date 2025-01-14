from flask import render_template, url_for, redirect, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from kactuz import app, database, bcrypt
from kactuz.models import Users, Address, Purchase
from kactuz.forms import FormLogin, FormCadastro, FormCompra, FormTamanho

@app.route("/")
def homepage():
	print(f"Usuário autenticado: {current_user.is_authenticated}")
	return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	form_login = FormLogin()
	if form_login.validate_on_submit():
		users = Users.query.filter_by(email=form_login.email.data).first()
		if users and bcrypt.check_password_hash(users.senha, form_login.senha.data):
			login_user(users)
			print(f"Usuário logado: {current_user}")
			print(f"Usuário autenticado: {current_user.is_authenticated}, ID: {current_user.get_id()}")
			return redirect(url_for("products", id_usuario=users.id, user=current_user))
	return render_template("login.html", form=form_login)

@app.route("/criarconta", methods=["GET", "POST"])
def cadastro():
	form_cadastro = FormCadastro()
	if form_cadastro.validate_on_submit():
		senha = bcrypt.generate_password_hash(form_cadastro.senha.data)
		users = Users(usuario=form_cadastro.usuario.data, senha=senha, email=form_cadastro.email.data)
		database.session.add(users)
		database.session.commit()
		login_user(users, remember=True)
		return redirect(url_for("products", id_usuario=users.id))
	return render_template("cadastro.html", form=form_cadastro)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for("homepage"))

@app.route("/products")
def products():
	print(f"Usuário autenticado: {current_user.is_authenticated}")
	return render_template("products.html")

@app.route("/camiseta", methods=["GET", "POST"])
def camisa():
	print(f"Usuário autenticado: {current_user.is_authenticated}")
	form_venda = FormTamanho()
	if form_venda.validate_on_submit():
		venda = Purchase(
			tamanho=form_venda.tamanho.data,
			id_usuario=current_user.id
		)
		database.session.add(venda)
		database.session.commit()
		return redirect(url_for('compra'))
	return render_template("camisa.html", form=form_venda)

@app.route("/endereco", methods=["GET", "POST"])
@login_required
def compra():
    form_compra = FormCompra()
    if form_compra.validate_on_submit():
        compra = Address(
            endereco=form_compra.address.data,
            numero=form_compra.numero.data,
            complemento=form_compra.complemento.data,
            cep=form_compra.cep.data,
            id_usuario=current_user.id
        )
        database.session.add(compra)
        database.session.commit()
        return redirect(url_for('form'))
    return render_template("compra.html", form=form_compra)




