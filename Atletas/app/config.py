import os
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'static', 'bagora.db')

class Config(object):
    SECRET_KEY = 'CambiarEstoPorUnaLlaveSegura'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG=0
    user_debugger=False
    _debugger__=False