from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, cls, obj_id):
        pass

    @abstractmethod
    def get_all(self, cls):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj):
        pass

    @abstractmethod
    def get_by_attribute(self, cls, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}  # Format : { 'ClassName': { id: obj } }

    def _get_class_storage(self, cls):
        class_name = cls.__name__
        if class_name not in self._storage:
            self._storage[class_name] = {}
        return self._storage[class_name]

    def add(self, obj):
        storage = self._get_class_storage(type(obj))
        storage[obj.id] = obj

    def get(self, cls, obj_id):
        storage = self._get_class_storage(cls)
        return storage.get(obj_id)

    def get_all(self, cls):
        return self._get_class_storage(cls)

    def update(self, obj_id, data):
        # Optionnel : implémenter si tu veux mettre à jour un objet directement
        pass

    def delete(self, obj):
        storage = self._get_class_storage(type(obj))
        if obj.id in storage:
            del storage[obj.id]

    def get_by_attribute(self, cls, attr_name, attr_value):
        storage = self._get_class_storage(cls)
        for obj in storage.values():
            if getattr(obj, attr_name) == attr_value:
                return obj
        return None

Storage = InMemoryRepository