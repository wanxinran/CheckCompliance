from flask import Blueprint, jsonify
from crud import crud_clause

userBp = Blueprint('user', __name__)


@userBp.route("/user/<string:user_id>", methods=['GET'])
def get_user(user_id: str):
    return jsonify(crud_clause.get(user_id))


@userBp.route("/get/name/<string:name>", methods=['GET'])
def get_name(name: str):
    return jsonify(crud_clause.get_user_by_name(name))


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
    clause = {
        "clause_no": "123",
        "clause_details": "123234"
    }
    return jsonify(crud_clause.create(**clause))

@userBp.route("/get")
def get():
    clause_no = {"clause_no": "6.1.2.1"}
    print(crud_clause.get(clause_no).to_dict()) # printout is correct, the website showed differently.
    return jsonify(crud_clause.get(clause_no).to_dict())


@userBp.route("/get_many", methods=['GET'])
def get_all():
    return jsonify(crud_clause.get_many(filters=[{"clause_no": "6.1.1.\d"}]))


@userBp.route("/update")
def update():
    new = {
        "clause_no": "6.1.1.1",
        "clause_details": "控制机房出入口应安排专人值守或配置电子门禁系统,控制、鉴别和记录进入的人员"
    }
    old = crud_clause.get({"clause_no": "6.1.1.1"})
    return jsonify(crud_clause.update(old, **new).to_dict())

@userBp.route("/delete")
def delete():
    old = crud_clause.get({"clause_no": "123"})
    crud_clause.delete(old)
