import secrets
from os import path

from flask import current_app, url_for
from flask_login import UserMixin, login_user, current_user
from PIL import Image
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app import bcrypt, db


class FindByMixin:
    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()


class SaveMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model, FindByMixin, SaveMixin, UserMixin):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)
    email = Column(String(250),
                   nullable=False)
    password = Column(String(250),
                      nullable=False)
    avatar = Column(String(250),
                    nullable=False,
                    default='default.png')
    accounts = relationship('Accounts', backref='user')

    @staticmethod
    def save_avatar(file):
        avatar = Image.open(file)

        avatar.thumbnail((100, 100))

        filename = f'{secrets.token_hex()}.png'

        upload_folder = current_app.config.get('UPLOAD_FOLDER')

        filepath = path.join(upload_folder, filename)

        avatar.save(filepath)

        return filename

    @property
    def url_avatar(self):
        return url_for('static', filename=f'uploads/{self.avatar}')

    def login(self, password, remember):
        check_password = bcrypt.check_password_hash(self.password, password)
        return check_password and login_user(self, remember)

    def update(self, name, email, avatar=None):
        self.name = name
        self.email = email

        if not avatar:
            return

        self.avatar = self.save_avatar(avatar)


class Accounts(db.Model, FindByMixin, SaveMixin):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)
    login = Column(String(250),
                   nullable=False)
    password = Column(String(250),
                      nullable=False)
    user_id = Column(Integer,
                     ForeignKey('user.id'))

    @classmethod
    def paginate(cls, page, per_page=1):
        return cls.query.filter_by(user_id=current_user.get_id()).paginate(page=page, per_page=per_page)

    def update(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
