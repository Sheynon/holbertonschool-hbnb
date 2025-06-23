from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self._users_store = {}
        self._amenity_store = {}

    def create_user(self, user_data):
        # Placeholder
        user = User(**user_data)
        self.user_repo.add(user)
        self._users_store[user.id] = user
        return user

    def get_place(self, place_id):
        # Placeholder
        return self.user_repo.get(user_id)

    def get_user(self, user_id):
        return self._users_store.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        self._amenity_store[amenity.id] = amenity
        return amenity

    def get_amenity(self, amenity_id):
        return self._amenity_store.get(amenity_id)

    def get_all_amenities(self):
        return list(self._amenity_store.values())

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self._amenity_store.get(amenity.id)
        if not amenity:
            return None
        for key, value in amenity_data.items():
            setattr(amenity, key, value)
        return amenity
