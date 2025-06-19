import re
from basse_model import BaseMode, BaseModel
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
        self.reviews = []
        self.amanities = []
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self.__name = value

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Description must be a non-empty string.")
        self.__description = value
    @property
    def longitude(self):
        return self.__longitude
    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("il manque la longitude")
        if not (-180 <= value <= 180):
            raise ValueError("il manque la valeur de longitude")
    
    @property
    def latitude(self):
        return self.__latitude
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("il manque la latitude")
        if not (-90 <= value <= 90):
            raise ValueError("il manque la valeur de latitude")
        self.__latitude = value