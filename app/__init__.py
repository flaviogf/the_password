from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.user.views import user
    app.register_blueprint(user)
    from app.accounts.views import accounts
    app.register_blueprint(accounts)

    return app
