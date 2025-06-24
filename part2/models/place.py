from models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = kwargs.get('title')
        self.description = kwargs.get('description', '')
        self.owner_id = kwargs.get('owner_id')
        self.amenities = kwargs.get('amenities', [])

        # Use setters for validation
        self.price = kwargs.get('price', 0.0)
        self.latitude = kwargs.get('latitude', 0.0)
        self.longitude = kwargs.get('longitude', 0.0)

    # --- Property setters/getters with validation ---
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = float(value)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = float(value)

    # --- Dictionary representation ---
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
                'amenities': self.amenities  # optionally list of amenity ids
            })
        return data
