class BaseViewData:
    def __init__(self, request) -> None:
        self.request = request
        self.error = None
        self.user_id = None
    
    def to_dict(self):
        return self.__dict__