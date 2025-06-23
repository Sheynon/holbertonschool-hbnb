# models/storage.py

class InMemoryStorage:
    def __init__(self):
        self.places = {}  # stockage en mémoire des objets Place (par exemple)

    def add_place(self, place):
        self.places[place.id] = place

    def get_place(self, place_id):
        return self.places.get(place_id)

    def get_all_places(self):
        return list(self.places.values())

    def update_place(self, place_id, data):
        place = self.get_place(place_id)
        if place:
            place.update(data)
            return place
        return None
