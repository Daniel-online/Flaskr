import functools
from flask import (Blueprint, Flask, render_template, flash, g, request, redirect, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix=('/auth'))

@bp.before_app_request
def load_logged_user():
	user_id = session.get('user_id')

	if user_id is None:
		g.user =None
	else:
		d.user = get_db( 'SELECT * FROM user WHERE ID = ?', (user_id)).fetchone()

@bp.route('/cadastro', methods = ['GET','POST'])
def register():
	if request == 'POST':
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')
		db = get_db()
		error = None


		if not username:
			error= "-Insira o nome de usuário, por favor-"
		elif not email:
			error = "-Insira o email, por favor-"
		elif not password:
			error = "-Insira a sua senha, por favor-"

		if error is None:
			try:
				db.execute (
					"INSERT INTO user (username,email, password) VALUES (?,?)",(username, email, generate_password_hash(password))
				)
				db.commit()

			except db.IntegrityError:
				error = f"Usuário {username} já está cadastrado"
		else:
			return redirect(url_for('auth.login'))

		flash(error)
		
	return render_template('auth/cadastro.html')


@bp.route('/login', methods=['GET','POST'])
def login():
	if request == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		db= get_db()
		error = None

		user = deb.execute( 'SELECT * FROM user WHERE email=*', (email)).fetchone()

		if user is None:
			error = "Não conseguimos encontrar sua conta"
		elif not check_password_hash (user['password'], password):
			error= "Senha incorreta, tente novamente"

		if error is None:
			session.clear()
			session['user-id'] = user['id']
			return redirect(url_for('index'))
		
		flash(error)

	return render_template('auth/login.html')

@bp.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.user is None:
			return redirect(url_for('auth.login'))
		return view(**kwargs)
	return wrapped_view