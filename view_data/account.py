from services import user_service
from view_data.base import BaseViewData


class AccountViewData(BaseViewData):
    def __init__(self, request):
        super().__init__(request)
        self.user = user_service.get_user(self.user_id)


class AccountRegisterViewData(BaseViewData):
    def __init__(self, request):
        super().__init__(request)

    async def load(self):
        form = await self.request.form()
        validated = self.validate_form(form)
        self.name = validated["name"]
        self.email = validated["email"]
        self.password = validated["password"]

    def validate_name(self, name):
        if not name:
            raise ValueError("not name")
        name = self.sanitize(name)
        if len(name) < 3:
            raise ValueError("Length must be >=8")
        return self.sanitize(name)

    def validate_email(self, email):
        if user_service.get_user_by_email(email):
            raise ValueError("User exists")
        return self.sanitize(email)

    def validate_pass(self, password):
        if len(password) < 4:
            raise ValueError("length < 8 chars")
        return self.sanitize(password)

    def validate_form(self, form):
        name = form.get("name")
        password = form.get("password")
        email = form.get("email")
        return {
            "name": self.validate_name(name),
            "email": self.validate_email(email),
            "password": self.validate_pass(password),
        }

    def sanitize(self, name: str):
        for i in "~!#$%^&*()_ -=+:;'\"\r\t\n":
            name = name.replace(i, "_")
        return name


class AccountLoginViewData(BaseViewData):
    def __init__(self, request):
        super().__init__(request)

    async def load(self):
        form = await self.request.form()
        validated = self.validate_form(form)
        self.email = validated["email"]
        self.password = validated["password"]

    def validate_name(self, name):
        if not name:
            raise ValueError("not name")
        name = self.sanitize(name)
        if len(name) < 3:
            raise ValueError("Length must be >=8")
        return self.sanitize(name)

    def validate_email(self, email):
        if user_service.get_user(pk=email):
            raise ValueError("User exists")
        return self.sanitize(email)

    def validate_pass(self, password):
        if len(password) < 4:
            raise ValueError("length < 8 chars")
        return self.sanitize(password)

    def validate_form(self, form):
        password = form.get("password")
        email = form.get("email")
        return {
            "email": self.validate_email(email),
            "password": self.validate_pass(password),
        }

    def sanitize(self, name: str):
        for i in "~!#$%^&*()_ -=+:;'\"\r\t\n":
            name = name.replace(i, "_")
        return name
