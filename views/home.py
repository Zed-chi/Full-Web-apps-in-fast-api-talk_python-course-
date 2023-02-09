from fastapi import APIRouter, Request

from settings import template_manager
from view_data.home import IndexViewData

home_router = APIRouter()


@home_router.get("/")
def index(request: Request):
    """Index page."""
    view_data = IndexViewData(request)
    context = {"request": request}
    context.update(view_data.to_dict())

    return template_manager.TemplateResponse(
        "./home/index.html", context=context
    )


@home_router.get("/about")
def about(request: Request):
    """About page."""
    view_data = IndexViewData(request)
    context = {"request": request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(
        "./home/about.html", context=context
    )
