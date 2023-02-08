from fastapi import APIRouter 


home_router = APIRouter()
@home_router.get("/")
def index(request:fastapi.Request):
    """Index page."""
    resp = "<h1>qwe</h1>"
    return template_manager.TemplateResponse(        
        "./index.html",
        context={"request":request}
    )


@home_router.get("/about")
def about(request:fastapi.Request):
    """Index page."""
    resp = "<h1>qwe</h1>"
    return template_manager.TemplateResponse(        
        "./index.html",
        context={"request":request}
    )