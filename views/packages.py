from fastapi import APIRouter, Request

from settings import template_manager
from view_data.package import DetailViewData, ListViewData

packages_router = APIRouter(prefix="/packages")


@packages_router.get("/")
def list_view(request: Request):
    """Index page."""
    view_data = ListViewData(request)
    context = {"request": request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(
        "./packages/list.html", context=context
    )


@packages_router.get("/{p_id}")
def detail_view(p_id: str, request: Request):
    """Index page."""
    view_data = DetailViewData(p_id, request)
    context = {"request": request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(
        "./packages/detail.html", context=context
    )
