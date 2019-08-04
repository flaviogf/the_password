import click
from flask.cli import with_appcontext

from app import bcrypt
from app.models import User


@click.command('', help='Create a user for access the app.')
@click.option('--name', prompt='Name')
@click.option('--email', prompt='Email')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True)
@with_appcontext
def create_user(name, email, password):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(name=name,
                email=email,
                password=password_hash)

    user.save()

    click.secho('user created successfully.', fg='green')
