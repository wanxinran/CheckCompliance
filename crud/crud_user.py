from crud.base import CRUDBase
from models import User


class CRUDUser(CRUDBase):

    def get_user_by_name(self, name):
        return self.db.query(User).filter(User.username == name)


crud_user = CRUDUser(User)
