from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from urllib.parse import quote_plus  # 解决密码中含有"@"的情况

app = Flask(__name__)

# HOSTNAME = "121.40.106.103"
# USERNAME = "wxr"
# PASSWORD = "wxr123456"
# DATABASE = "comprehensive-alg"

HOSTNAME = "127.0.0.1"  # MySQL所在主机名
PORT = 3306
USERNAME = "root"
PASSWORD = "mysql@2022"
DATABASE = "pracDB"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{USERNAME}:{quote_plus(PASSWORD)}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}?charset=utf8'

db = SQLAlchemy(app)  # SQLAlchemy从app.config里读取: 数据库连接的信息


# # 测试是否连接成功
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone()) #返回(1,)
class User(db.Model):
    __tablename__ = "user-table"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)  # varchar
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()  # 把所有表加到数据库里


@app.route("/user/add") #CRUD都可以这样写
def add_user():
    user = User(username="Wan Xinran", password="wxr@2023")
    db.session.add(user)
    db.session.commit()
    return "New user added!"

@app.route("/user/query")
def query_user():
    user = User.query.get(1) # query based on 主键
    # users = User.query.all() # fetch all users
    print(f"{user.id}: {user.username} - {user.password}")
    return "Query succeeded!"

@app.route("/user/multi_query")
def multi_query_user():
    users = User.query.filter_by(username="Wan Xinran")
    for user in users:
        print(f"{user.id}: {user.username} - {user.password}")
    return "Multiple query succeeded!"

@app.route("/user/update")
def query_user():
    user = User.query.filter_by(username="Wan Xinran").first()
    user.password = "newPassword"
    db.session.commit()
    return "User updated succeeded!"

@app.route("/user/delete")
def query_user():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commmit()
    return "User deleted succeeded!"



if __name__ == "__main__":
    app.run(debug=True)
