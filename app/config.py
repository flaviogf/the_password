class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:C894aH86dPAP5V0uuEiV@default.c4wkgwgnxr0p.us-east-1.rds.amazonaws.com/the_password'
