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
    # verifie que le nom est une chaine de caractere non vide
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self.__name = value

    @property
    # verifie que la description est une chaine de caractere non vide
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Description must be a non-empty string.")
        self.__description = value

    @property
    # verifie que la longitude est un nombre entre -180 et 180
    # verifie que la longitude à bien été initialisée
    def longitude(self):
        return self.__longitude
    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("il manque la longitude")
        if not (-180 <= value <= 180):
            raise ValueError("il manque la valeur de longitude")
    
    @property
    # verifie que la latitude est un nombre entre -90 et 90
    # verifie que la latitude à bien été initialisée
    def latitude(self):
        return self.__latitude
    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("il manque la latitude")
        if not (-90 <= value <= 90):
            raise ValueError("il manque la valeur de latitude")
        self.__latitude = value

    @property
    # verifie que le prix est un nombre positif
    # verifie que le prix à bien été initialisé
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if not isinstance(value, (self, float)):
            raise TypeError("il manque le prix")
        if value < 1:
            raise ValueError("le prix doit être positif")
        self.__price = value
    @property
    # verifie que le owner est une chaine de caractere non vide
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("")
        self.__owner = value