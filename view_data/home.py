from view_data.base import BaseViewData
from services import package_service, user_service


class IndexViewData(BaseViewData):
    def __init__(self, request):
        super().__init__(request)

        self.package_count = package_service.package_count()
        self.user_count = user_service.user_count()
        self.release_count = package_service.release_count()
        self.latest_releases = package_service.latest_releases()