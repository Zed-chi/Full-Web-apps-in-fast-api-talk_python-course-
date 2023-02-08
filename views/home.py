from fastapi import APIRouter, Request 
from settings import template_manager


home_router = APIRouter()
@home_router.get("/")
def index(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./home/index.html",
        context={"request":request}
    )


@home_router.get("/about")
def about(request:Request):
    """About page."""
    return template_manager.TemplateResponse(        
        "./home/about.html",
        context={"request":request}
    )