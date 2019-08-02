from os import environ

from app import create_app

app = create_app(config=environ.get('CONFIG', 'app.config.Development'))
