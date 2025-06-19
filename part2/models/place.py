import re
from basse_model import BaseMode
from user import reviews

class Place(BaseModel):
    def __init__(self, name, description, longitude, latitude, price, owner):
        super().__init__()
        self.name = name
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.price = price
        self.owner = owner
        