from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('Username', 
    [ 
        validators.DataRequired(message = 'Ingresa un username'),
        validators.length(min=4, max=24, message='Username no valido.')
    ])
    password = PasswordField('Password',
    [
        validators.DataRequired(message = 'Ingresa el password')
    ])

class BuscadorForm(Form):
    Buscar = StringField('Buscar',
    [
        validators.DataRequired(message = 'Pero decíme qué querés buscar.')
    ])