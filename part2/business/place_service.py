from models import storage
from models.place import Place
from models.user import User
from models.amenity import Amenity

class PlaceService:

    @staticmethod
    def create_place(data):
        required = ['name', 'owner_id']
        for field in required:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        if 'price_by_night' in data and not isinstance(data['price_by_night'], int):
            raise ValueError("price_by_night must be an integer")
        if 'latitude' in data and not isinstance(data['latitude'], float):
            raise ValueError("latitude must be a float")
        if 'longitude' in data and not isinstance(data['longitude'], float):
            raise ValueError("longitude must be a float")

        owner = storage.get(User, data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")

        new_place = Place(**data)
        storage.new(new_place)
        storage.save()
        return new_place

    @staticmethod
    def get_place(place_id=None):
        if place_id:
            place = storage.get(Place, place_id)
            if not place:
                raise ValueError("Place not found")
            return place
        return storage.all(Place).values()

    @staticmethod
    def update_place(place_id, data):
        place = storage.get(Place, place_id)
        if not place:
            raise ValueError("Place not found")

        for key, value in data.items():
            if key in ['id', 'owner_id', 'created_at', 'updated_at']:
                continue
            setattr(place, key, value)
        
        storage.save()
        return place
