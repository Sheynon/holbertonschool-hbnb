from models.base_model import BaseModel

class Place(BaseModel):
    """herite de BaseModel"""
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner

        if not title or len(title) > 100:
            raise ValueError("il faut un titre maximum de 100 caractères ou titre")
        if not description:
            raise ValueError("il faut une description")
        if price <= 0:
            raise ValueError("il faut un prix supérieur à 0")
        if not -90 < latitude > 90:
            raise ValueError("il faut une latitude entre -90 et 90")
        if not -180 < longitude > 180:
            raise ValueError("il faut une longitude entre -180 et 180")
        if not isinstance(owner, BaseModel):
            raise ValueError("il faut un owner de type BaseModel")
