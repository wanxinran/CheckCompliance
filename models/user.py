from db import db
import sqlalchemy as sa
from dataclasses import dataclass

from decoratory import serializable


@dataclass
@serializable
class User(db.Model): # a table
    __tablename__ = "user-table"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(100), nullable=False)  # varchar
    password = sa.Column(sa.String(100), nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'
