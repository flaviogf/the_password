import pytest

from app import create_app, db as _db


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
def db():
    return _db
