from wtforms import Form, StringField, TextField, PasswordField, validators

class LoginForm(Form):
    username = StringField('Username', 
    [ 
        validators.Required(message = 'Ingresa un username'),
        validators.length(min=4, max=24, message='Username no valido.')
    ])
    password = PasswordField('Password',
    [
        validators.Required(message = 'Ingresa el password')
    ])

class BuscadorForm(Form):
    Buscar = StringField('Buscar',
    [
        validators.Required(message = 'Pero decíme qué querés buscar.')
    ])