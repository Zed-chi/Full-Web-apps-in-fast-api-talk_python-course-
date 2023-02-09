def release_count():
    return 2


def package_count():
    return 1


def latest_releases(limit=5):
    return [
        {"id": 1, "name": "qwe", "description": "test packege for testing"}
    ]


def get_package(pk=None):
    if not pk:
        return None
    return None


def get_latest_release(package):
    pass
