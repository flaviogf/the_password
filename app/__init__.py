from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    def register_extensions():
        db.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        from app.models import User
        login_manager.user_loader(lambda user_id: User.query.get(user_id))
        login_manager.login_view = 'user.login'
        login_manager.login_message_category = 'danger'

    def register_blueprints():
        from app.user.views import user
        app.register_blueprint(user)
        from app.accounts.views import accounts
        app.register_blueprint(accounts)

    def register_commands():
        from app.commands import create_user
        app.cli.add_command(create_user)

    register_extensions()
    register_blueprints()
    register_commands()

    return app
