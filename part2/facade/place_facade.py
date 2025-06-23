from business.place_service import PlaceService

class PlaceFacade:

    @staticmethod
    def create(data):
        return PlaceService.create_place(data)

    @staticmethod
    def retrieve(place_id=None):
        return PlaceService.get_place(place_id)

    @staticmethod
    def update(place_id, data):
        return PlaceService.update_place(place_id, data)
