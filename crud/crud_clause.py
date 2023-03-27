from crud.base import CRUDBase
from models import Clause


class CRUDClause(CRUDBase):

    def get_clause_by_name(self, c_no):
        return [u.to_dict() for u in self.db.query(Clause).filter_by(clause_no=c_no).all()]


crud_clause = CRUDClause(Clause)
