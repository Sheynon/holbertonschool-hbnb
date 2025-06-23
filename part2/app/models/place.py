from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel, Base):
    __tablename__ = 'places'

    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    owner_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    owner = relationship("User")
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
