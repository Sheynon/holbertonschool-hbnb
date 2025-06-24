import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.place import Place
from models.user import User
from models.amenity import Amenity
from storage import Storage

class HBnBFacade:
    def __init__(self):
        self.storage = Storage()

    def create_place(self, place_data):
        try:
            owner = self.storage.get(User, place_data['owner_id'])
            if not owner:
                raise ValueError("Owner not found")

            amenities = [
                self.storage.get(Amenity, a_id)
                for a_id in place_data.get('amenities', [])
            ]
            if None in amenities:
                raise ValueError("One or more amenities not found")

            place = Place(**place_data)
            place.amenities = amenities
            self.storage.new(place)
            self.storage.save()
            return place
        except Exception as e:
            raise e

    def get_place(self, place_id):
        place = self.storage.get(Place, place_id)
        if not place:
            raise ValueError("Place not found")
        return place

    def get_all_places(self):
        return self.storage.all(Place).values()

    def update_place(self, place_id, place_data):
        place = self.storage.get(Place, place_id)
        if not place:
            raise ValueError("Place not found")
        for key, value in place_data.items():
            if key in ['title', 'description', 'price', 'latitude', 'longitude']:
                setattr(place, key, value)
        self.storage.save()
        return place
