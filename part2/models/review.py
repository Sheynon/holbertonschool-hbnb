from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from os import getenv

class Review(BaseModel):
    __tablename__ = 'reviews'  # Ajout nécessaire pour SQLAlchemy

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        text = kwargs.get('text')
        if not text or len(text) > 1024:
            raise ValueError("Review text requis et ≤ 1024 caractères")
        self.text = text
        self.place_id = kwargs.get('place_id')
        self.user_id = kwargs.get('user_id')

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'place_id': self.place_id,
            'user_id': self.user_id
        }
