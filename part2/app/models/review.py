from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    user = relationship("User")
    place = relationship("Place", back_populates="reviews")
