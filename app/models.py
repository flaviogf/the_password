from app import db
from sqlalchemy import Column, String, Integer


class User(db.Model):
    id = Column(Integer,
                primary_key=True)
    name = Column(String(250),
                  nullable=False)
    email = Column(String(250),
                   nullable=False)
    password = Column(String(250),
                      nullable=False)
