from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from urllib.parse import quote_plus # 解决密码中含有"@"的情况

app = Flask(__name__)

# HOSTNAME = "121.40.106.103"
# USERNAME = "wxr"
# PASSWORD = "wxr123456"
# DATABASE = "comprehensive-alg"

HOSTNAME = "127.0.0.1" #MySQL所在主机名
PORT = 3306
USERNAME = "root"
PASSWORD = "mysql@2022"
DATABASE = "pracDB"


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{quote_plus(PASSWORD)}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'

db = SQLAlchemy(app) #SQLAlchemy从app.config里读取数据库连接的信息
# 测试是否连接成功
# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone()) #返回(1,)



if __name__ == "__main__":
    app.run(debug=True)