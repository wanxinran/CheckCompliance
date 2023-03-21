from flask import Blueprint
from crud import crud_user

userBp = Blueprint('用户模块', __name__)


@userBp.route("/user/<id>")
def get_user(_id: str):
    return crud_user.get(_id)
