from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = self._create_password(password)

    def _create_password(self, password):
        return generate_password_hash(password, "pbkdf2:sha256")

    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Atletas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64))
    pais = db.Column(db.String(16))
    foto_url = db.Column(db.String(32)) 