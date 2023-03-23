from db import db
import sqlalchemy as sa


class Test(db.Model):
    __tablename__ = "test"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100), nullable=False)  # varchar
    text = sa.Column(sa.String(200), nullable=False)
    date = sa.Column(sa.DateTime(), nullable=False)

    def __repr__(self):
        return f'<Test {self.name}>'
