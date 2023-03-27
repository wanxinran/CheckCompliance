from flask import Blueprint, jsonify
from crud import crud_user

userBp = Blueprint('user', __name__)


@userBp.route("/user/<string:user_id>", methods=['GET'])
def get_user(user_id: str):
    return jsonify(crud_user.get(user_id))


@userBp.route("/get/name/<string:name>", methods=['GET'])
def get_name(name: str):
    return jsonify(crud_user.get_user_by_name(name))


@userBp.route("/")
def root():
    return "hello word!"


@userBp.route('/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)


@userBp.route("/add")
def add():
    user = {
        "username": "123",
        "password": "123234"
    }
    return jsonify(crud_user.create(**user))

@userBp.route("/get")
def get():
    return jsonify(crud_user.get(5).to_dict())


@userBp.route("/get_many", methods=['GET'])
def get_all():
    return jsonify(crud_user.get_many(filters=[{"username": "123"}]))

@userBp.route("/update")
def update():
    new = {
        "username": "Cindy",
        "password": "230906"
    }
    old = crud_user.get(6)
    return jsonify(crud_user.update(old, **new).to_dict())

@userBp.route("/delete")
def delete():
    old = crud_user.get(9)
    crud_user.delete(old)
    return None
