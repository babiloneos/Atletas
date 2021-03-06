class Config(object):
    SECRET_KEY = 'CambiarEstoPorUnaLlaveSegura'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///static/bagora.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG=0
    user_debugger=False
    _debugger__=False