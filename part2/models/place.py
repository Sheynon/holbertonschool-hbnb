from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    __tablename__ = 'places'

    title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", back_populates="place", cascade="all, delete")

    def to_dict(self, summary=False):
        data = {
            'id': self.id,
            'title': self.title,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
        if not summary:
            data.update({
                'description': self.description,
                'price': self.price,
                'owner_id': self.owner_id,
                'reviews': [review.id for review in self.reviews]
            })
        return data
