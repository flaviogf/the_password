import click
from flask import Flask
from flask.cli import with_appcontext
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


@click.command('', help='Create a user for access the app.')
@click.option('--name', prompt='Name')
@click.option('--email', prompt='Email')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True)
@with_appcontext
def create_user(name, email, password):
    from app.models import User

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(name=name,
                email=email,
                password=password_hash)

    db.session.add(user)

    db.session.commit()

    click.secho('user created successfully.', fg='green')


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.models import User
    login_manager.user_loader(lambda user_id: User.query.get(user_id))
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'danger'

    from app.user.views import user
    app.register_blueprint(user)
    from app.accounts.views import accounts
    app.register_blueprint(accounts)

    app.cli.add_command(create_user)

    return app
