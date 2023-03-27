from db import db
import sqlalchemy as sa
from decoratory import serializable
from dataclasses import dataclass


@dataclass
@serializable
class Clause(db.Model):
    __tablename__ = "details"
    _id = sa.Column(sa.Integer)
    std_no = sa.Column(sa.String(20))
    enforced_date = sa.Column(sa.String(20))
    level = sa.Column(sa.Integer)
    clause_no = sa.Column(sa.String(20), primary_key=True)
    clause_details = sa.Column(sa.String(520))

    def __init__(self, clause_no: str, clause_details: str):
        # self.std_no = std_no
        # self.enforced_date = enforced_date
        # self.level = level
        self.clause_no = clause_no
        self.clause_details = clause_details

    def __repr__(self):
        return f'<Clause {self.clause_no}.>'
