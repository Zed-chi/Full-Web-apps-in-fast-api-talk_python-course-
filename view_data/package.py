from services import package_service, user_service
from view_data.base import BaseViewData


class DetailViewData(BaseViewData):
    def __init__(self, p_id, request):
        super().__init__(request)
        self.package = package_service.get_package(pk=p_id)
        if not self.package:
            return None


class ListViewData(BaseViewData):
    def __init__(self, request):
        super().__init__(request)

        self.package_count = package_service.package_count()
        self.user_count = user_service.user_count()
        self.release_count = package_service.release_count()
        self.latest_releases = package_service.latest_releases()
