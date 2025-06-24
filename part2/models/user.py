from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(50), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name = kwargs.get('name')
        if not name or len(name) > 50:
            raise ValueError("name requis et ≤ 50 caractères")
        self.name = name
