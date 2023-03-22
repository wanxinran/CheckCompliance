from typing import Optional

from pymysql import cursors, connect
from flask import Flask, g, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Mysql:
    db = None

    def __init__(self, app: Optional[Flask] = None):
        self.app = app
        config = {
            # "HOST": "127.0.0.1:3306",
            "HOST": "192.168.31.31",
            "USER": "root",
            "PASSWORD": "mysql@2022",
            "DB": "mysql"
        }

        if "MYSQL" not in app.config:
            app.config.setdefault("MYSQL", config)
            app.config.setdefault("SQLALCHEMY_DATABASE_URI", f"mysql+pymysql:// \
                {current_app.config['MYSQL']['USER']}:{current_app.config['MYSQL']['PASSWORD']}\
                @{current_app.config['MYSQL']['HOST']}/{current_app.config['MYSQL']['DB']}?charset=utf8mb4",
                                  echo=current_app.config['DEBUG'])

        self.db = SQLAlchemy(app)
        g.setdefault('session', self.db.session)
        g.setdefault('db', self.db)

    def init_table(self):
        with self.app.app_context():
            self.db.create_all()


def get_db():
    if 'db' in g:
        return g.db
    raise Exception("Database initialization error")


def get_session():
    """
    Acquire session
    """
    if 'session' not in g:
        engine = create_engine(
            f"mysql+pymysql:// \
            {current_app.config['MYSQL']['USER']}:{current_app.config['MYSQL']['PASSWORD']}\
            @{current_app.config['MYSQL']['HOST']}/{current_app.config['MYSQL']['DB']}?charset=utf8mb4",
            echo=current_app.config['DEBUG']
        )

        Session = sessionmaker(bind=engine)
        g.session = Session()
    return g.session


def get_connection():
    """
    pymysql connection
    """
    if 'py_db' not in g:
        config = current_app.config['MYSQL']
        g.db = connect(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASSWORD'],
            db=config['DB'],
            charset=config.get('CHARSET', 'utf8mb4'),
            cursorclass=cursors.DictCursor
        )
    return g.py_db


def close_connection():
    """
    close
    """
    g.pop('db', None)
    db = g.pop('py_db', None)

    if db is not None:
        db.close()

    session = g.pop('session', None)

    if session is not None:
        session.close()
