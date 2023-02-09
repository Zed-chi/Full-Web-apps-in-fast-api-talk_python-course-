from fastapi import APIRouter, Request
from settings import template_manager

packages_router = APIRouter(prefix="/packages")



@packages_router.get("/")
def list_view(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./packages/list.html",
        context={"request":request}
    )

@packages_router.get("/{p_id}")
def detail_view(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./packages/detail.html",
        context={"request":request}
    )