from db import db
import sqlalchemy as sa


class User(db.Model):
    __tablename__ = "user-table"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(100), nullable=False)  # varchar
    password = sa.Column(sa.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
