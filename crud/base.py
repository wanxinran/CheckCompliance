from typing import TypeVar, Type, Union, List, Dict, Any
from sqlalchemy.ext.declarative import declarative_base
from db import session

# constrained type
Base = declarative_base()
ModelType = TypeVar("ModelType", bound=Base)
db = session


class CRUDBase:
    """
    crud base
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.db = db

    def get(self, clause_no) -> Union[ModelType, None]:
        # clause_no = {"clause_no": "6.1.1.1"}, 是个字典
        return db.query(self.model).get(clause_no)

    def get_many(self, filters: List[Dict[str, Any]] = None, offset: int = 0, limit: int = 10) -> List[ModelType]:
        query = db.query(self.model)
        if filters:
            for itr in filters:
                column = getattr(self.model, list(itr.keys())[0])
                # query = query.filter(column == list(itr.values())[0])
                query = query.filter(column.op('regexp')(list(itr.values())[0])) # 可以用正则表达式
        return [c.to_dict() for c in query.offset(offset).limit(limit).all()]

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance.to_dict()

    def update(self, obj: ModelType, commit: bool = True, **kwargs) -> ModelType:
        for key, value in kwargs.items():
            setattr(obj, key, value)
        if commit:
            db.commit()
            db.refresh(obj)
        return obj

    def delete(self, obj: ModelType, commit: bool = True):
        db.delete(obj)
        if commit:
            db.commit()
