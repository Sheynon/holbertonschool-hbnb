from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        if not text:
            raise ValueError("text requis")
        if not (1 <= rating <= 5):
            raise ValueError("rating doit être entre 1 et 5")
        if not isinstance(place, BaseModel):
            raise ValueError("place invalide")
        if not isinstance(user, BaseModel):
            raise ValueError("user invalide")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user