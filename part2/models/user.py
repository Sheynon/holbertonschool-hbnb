from models.base_model import BaseModel

class User(BaseModel):
    _emails = set()  # Pour garantir l’unicité

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError("first_name requis et ≤ 50 caractères")
        if not last_name or len(last_name) > 50:
            raise ValueError("last_name requis et ≤ 50 caractères")
        if not email or '@' not in email:
            raise ValueError("email requis et doit être valide")
        if email in User._emails:
            raise ValueError("email déjà utilisé")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        User._emails.add(email)