from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from app import bcrypt, db


class User(db.Model, UserMixin):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)
    email = Column(String(250),
                   nullable=False)
    password = Column(String(250),
                      nullable=False)

    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password, password)
