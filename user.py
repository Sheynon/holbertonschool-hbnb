import re
from models.base_model import BaseModel

class user(BaseModel):
    """ erite la classe de BaseModel """
    _emails = set()

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        if not first_name or len(first_name) > 20:
            raise ValueError("vous devez saisir un prénom de 20 caractères maximum ou rajouter un prenom")
        if not last_name or len(last_name) > 20:
            raise ValueError("vous devez saisir un nom de 20 caractères maximum ou rajouter un nom")
        if not email or '@' not in email:
            raise ValueError("email requis et doit être valide")
        if email in user._emails:
            raise ValueError("email déjà utilisé")
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        user._emails.add(email)

    def is_admin(self):
        return self.is_admin