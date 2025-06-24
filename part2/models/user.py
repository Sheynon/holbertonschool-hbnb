from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, name):
        super().__init__()
        if not name or len(name) > 50:
            raise ValueError("name requis et ≤ 50 caractères")
        self.name = name
