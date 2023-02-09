from datetime import datetime


class Package:
    def __init__(self, name) -> None:
        self.name = name
        self.summary = None
        self.description = None
        self.home_page = None
        self.license = None
        self.author = None
        self.maintainers = None


class Release:
    def __init__(self, version) -> None:
        self.version = version
        self.released_at = datetime.now()
