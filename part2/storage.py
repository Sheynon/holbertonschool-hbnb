from models.base_model import BaseModel

class Storage:
    def __init__(self):
        self.__data = {
            'Place': {},
            'User': {},
            'Amenity': {}
        }

    def all(self, cls):
        return self.__data.get(cls.__name__, {})

    def get(self, cls, obj_id):
        return self.__data.get(cls.__name__, {}).get(obj_id)

    def new(self, obj):
        self.__data[obj.__class__.__name__][obj.id] = obj

    def save(self):
        pass

