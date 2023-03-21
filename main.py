from flask import Flask

from db import Mysql, close_connection
from api import bp

app = Flask(__name__)
app.register_blueprint(bp)

# 初始化数据库
mysql = Mysql(app)
mysql.init_table()

if __name__ == "main":
    app.run(debug=True)


@app.teardown_appcontext()
def close_db():
    """
    close database.
    """
    close_connection()
