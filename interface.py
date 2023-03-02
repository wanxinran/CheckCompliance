from flask import Flask

app = Flask(__name__) #app.py这个模块

@app.route("/") #定路由的装饰器
def hello_world():
    return "<p>Hello, flask!</p>"


if __name__ == "__main__":
    app.run(debug=True)