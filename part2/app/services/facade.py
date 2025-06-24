import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
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

    def create_review(self, review_data):
        user = self.storage.get(User, review_data.get('user_id'))
        place = self.storage.get(Place, review_data.get('place_id'))
        if not user or not place:
            raise ValueError("Invalid user_id or place_id")
        if not isinstance(review_data.get('rating'), int) or not (1 <= review_data['rating'] <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")

        review = Review(**review_data)
        self.storage.new(review)
        self.storage.save()
        return review

    def get_review(self, review_id):
        review = self.storage.get(Review, review_id)
        if not review:
            raise LookupError("Review not found")
        return review

    def get_all_reviews(self):
        return self.storage.all(Review).values()

    def get_reviews_by_place(self, place_id):
        place = self.storage.get(Place, place_id)
        if not place:
            raise LookupError("Place not found")
        return [r for r in self.storage.all(Review).values() if r.place_id == place_id]

    def update_review(self, review_id, review_data):
        review = self.storage.get(Review, review_id)
        if not review:
            raise LookupError("Review not found")
        for key, value in review_data.items():
            if key in ['text', 'rating']:
                setattr(review, key, value)
        self.storage.save()
        return review

    def delete_review(self, review_id):
        review = self.storage.get(Review, review_id)
        if not review:
            raise LookupError("Review not found")
        self.storage.delete(review)
        self.storage.save()

facade = HBnBFacade()
