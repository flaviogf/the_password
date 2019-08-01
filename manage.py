from app import create_app
from os import environ


app = create_app(config=environ.get('CONFIG', 'app.config.Development'))
