from datetime import datetime


class User:
    def __init__(self, name, email, hashed_pass) -> None:
        self.pk = email
        self.name = name
        self.email = email
        self.password = hashed_pass
        self.created_at = datetime.now()
        self.last_logged = None

    def to_dict(self):
        return self.__dict__