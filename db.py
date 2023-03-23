from typing import Optional

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, Session


class Mysql:
    db = None
    app = None

    def __init__(self):
        self.config = {
            # "HOST": "127.0.0.1:3306",
            "HOST": "192.168.31.31",
            "USER": "root",
            "PASSWORD": "mysql@2022",
            "DB": "mysql"
        }

        self.db = SQLAlchemy()

    def init_app(self, app: Optional[Flask] = None):
        self.app = app
        if "MYSQL" not in app.config:
            app.config.setdefault("MYSQL", self.config)
            app.config.setdefault("SQLALCHEMY_DATABASE_URI",
                                  f"mysql+pymysql://{app.config['MYSQL']['USER']}:{app.config['MYSQL']['PASSWORD']}\
                                  @{app.config['MYSQL']['HOST']}/{app.config['MYSQL']['DB']}?charset=utf8mb4")

        self.db.init_app(app)
        self.init_db()

    def init_table(self):
        self.db.create_all()

    def init_db(self):
        if 'db' not in g:
            g.setdefault('db', self.db)

        if 'session' not in g:
            g.setdefault('session', self.db.session)


def close_connection():
    """
    close
    """
    g.pop('db', None)
    py_db = g.pop('py_db', None)

    if py_db is not None:
        py_db.close()

    _session = g.pop('session', None)

    if _session is not None:
        _session.close()


mysql = Mysql()
db: Optional[SQLAlchemy] = mysql.db
session: Optional[scoped_session[Session]] = mysql.db.session
