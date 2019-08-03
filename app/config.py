class Config:
    SECRET_KEY = '0f1b007cd45ecd1b2da1084e2e9e5913e64b763f66c50942aa5ca3ff33e95211'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    LOGIN_DISABLED = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/the_password'
