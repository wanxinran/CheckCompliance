from crud.base import CRUDBase
from models import User


class CRUDUser(CRUDBase):

    def get_user_by_name(self, name):
        return [u.to_dict() for u in self.db.query(User).filter_by(username=name).all()]


crud_user = CRUDUser(User)
