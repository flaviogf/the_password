from unittest.mock import patch

import pytest

from app import bcrypt as _bcrypt
from app import create_app
from app import db as _db
from app.models import User


@pytest.yield_fixture
def app():
    app = create_app(config='config.Testing')

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    return _db


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def bcrypt(app):
    return _bcrypt


@pytest.yield_fixture
def user(app, bcrypt):
    password = bcrypt.generate_password_hash('test')

    naruto = User(name='naruto',
                  email='naruto@gmail.com',
                  password=password)

    with patch('flask_login.utils._get_user', new=lambda: naruto):
        yield naruto
