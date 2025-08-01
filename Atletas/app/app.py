from flask import Flask, render_template,  request, session, redirect, url_for, g, flash, abort
from config import DevelopmentConfig
from models import db, Users, Atletas
from werkzeug.debug import DebuggedApplication
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.debug = False

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    if 'username' in session and request.endpoint in ['index', 'login']:
        return redirect(url_for('buscador'))
    elif 'username' not in session and request.endpoint in ['buscador', 'flag']:
        return redirect(url_for('index'))
    elif request.path.__contains__('/static/img/') or request.path.__contains__('/static/css/'):
        pass
    elif (request.endpoint not in ['buscador', 'flag', 'index', 'login', 'logout']):
        abort(404)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        user = Users.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            session['username'] = username
            return redirect(url_for('buscador'))
        else:
            error_message="Usuario o contraseña incorrecto."
            flash(error_message)
    return render_template('login.html', form = login_form)

@app.route('/buscador', methods=['POST', 'GET'])
def buscador():
    buscador_form = forms.BuscadorForm(request.form)
    buscar = request.args.get('Buscar')
    resultado = None
    if request.method == "GET" and buscar is not None:
        if buscar.isspace():
            error_message="Busqueda vacía."
            flash(error_message)
            buscar=None
        else:
            connection = db.engine.connect()
            resultado = connection.execute(
            "SELECT * FROM 'atletas' where nombre like '%"+buscar+"%' or pais like '%"+buscar+"%' ORDER BY atletas.nombre ASC")
            return render_template('buscador.html', busqueda=buscar, resultado=resultado, form=buscador_form)
    return render_template('buscador.html', busqueda=buscar, form=buscador_form)

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index'))

@app.route('/flag')
def flag():
    if session['username'] not in ['admin']:
        abort(404)
    else:
        return render_template('flag.html')

@app.after_request
def after_request(response):
    
    return response



if __name__ == '__main__':
    db.init_app(app)

    with app.app_context():
        db.create_all()
      
    application = DebuggedApplication(app, False)
    app.run(debug=False, use_evalex=False, port=5000)
 