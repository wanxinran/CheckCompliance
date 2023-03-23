def serializable(cls):
    def to_dict(self):
        return { c.name: getattr(self, c.name) for c in self.__table__.columns }

    cls.to_dict = to_dict
    return cls
