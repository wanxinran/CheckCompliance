from db import get_db

db = get_db()


class User(db.Model):
    __tableName__ = "user-table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)  # varchar
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
