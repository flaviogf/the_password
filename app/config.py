class Config:
    SECRET_KEY = '0f1b007cd45ecd1b2da1084e2e9e5913e64b763f66c50942aa5ca3ff33e95211'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:C894aH86dPAP5V0uuEiV@default.c4wkgwgnxr0p.us-east-1.rds.amazonaws.com/the_password'
