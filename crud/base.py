from typing import TypeVar, Type, Union, List, Dict, Any
from sqlalchemy.ext.declarative import declarative_base
from db import get_session

# constrained type
Base = declarative_base()
ModelType = TypeVar("ModelType", bound=Base)
db = get_session()


class CRUDBase:
    """
    curd base
    """

    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.db = db

    def get(self, _id) -> Union[ModelType, None]:
        return db.query(self.model).get(_id)

    def get_many(self, filters: List[Dict[str, Any]] = None, offset: int = 0, limit: int = 10) -> List[ModelType]:
        query = db.query(self.model)
        if filters:
            for itr in filters:
                column = getattr(self.model, itr['field'])
                query = query.filter(column == itr['value'])
        return query.offset(offset).limit(limit).all()

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

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
