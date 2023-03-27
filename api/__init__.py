from .endpoints import clause
from flask import Blueprint

bp = Blueprint('API', __name__)
bp.register_blueprint(clause.userBp)
