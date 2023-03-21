from .endpoints import user
from flask import Blueprint

bp = Blueprint('API', __name__)
bp.register_blueprint(user.userBp)
