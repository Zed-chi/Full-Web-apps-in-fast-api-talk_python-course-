from infrastructure import cookie_auth


class BaseViewData:
    def __init__(self, request) -> None:
        self.request = request
        self.error = None
        self.user_id = cookie_auth.get_user_id_from_auth_cookie(
            self.request
        )
        self.is_logged_in = self.user_id is not None
        self.error = ""

    def to_dict(self):
        return self.__dict__
