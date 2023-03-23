from flask import Blueprint, jsonify
from crud import crud_user

userBp = Blueprint('user', __name__)


@userBp.route("/user/<id>", methods=['GET'])
def get_user(_id: str):
    return crud_user.get(_id)


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
    temp = crud_user.get(5)
    print(temp, type(temp))
    return jsonify(temp.username)

@userBp.route("/get_many", methods=['GET'])
def get_all():
    temp = crud_user.get_many(filters=[{"username": "123"}])
    return jsonify([t.username for t in temp])





