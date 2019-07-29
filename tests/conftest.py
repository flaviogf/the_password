import pytest

from app import create_app
from app import db as _db
from app import bcrypt as _bcrypt


@pytest.yield_fixture
def app():
    app = create_app(config='app.config.Testing')

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
