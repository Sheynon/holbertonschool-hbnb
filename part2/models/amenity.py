from models.base_model import BaseModel
from sqlalchemy import Column, String

class Amenity(BaseModel):
    __tablename__ = 'amenities'  # Obligatoire

    name = Column(String(50), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Gestion manuelle de l’attribut `name` avec validation
        name = kwargs.get('name')
        if not name or len(name) > 50:
            raise ValueError("name requis et ≤ 50 caractères")
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
