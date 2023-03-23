from flask import Flask
from flasgger import Swagger
from db import mysql, close_connection
from api import bp

app = Flask(__name__)
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/docs/"
}
Swagger(app, config=swagger_config)
with app.app_context():
    mysql.init_app(app)
    app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(port=9001, debug=True)


@app.teardown_appcontext
def close_db(exception):
    """
    close database.
    """
    close_connection()
