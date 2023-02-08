from fastapi import APIRouter 


account_router = APIRouter(prefix="/account")
@account_router.get("/")
def account(request:fastapi.Request):
    """Index page."""
    resp = "<h1>qwe</h1>"
    return template_manager.TemplateResponse(        
        "./index.html",
        context={"request":request}
    )


@account_router.get("/register")
def register(request:fastapi.Request):
    """Index page."""
    resp = "<h1>qwe</h1>"
    return template_manager.TemplateResponse(        
        "./index.html",
        context={"request":request}
    )


@account_router.get("/login")
def login(request:fastapi.Request):
    """Index page."""
    resp = "<h1>qwe</h1>"
    return template_manager.TemplateResponse(        
        "./index.html",
        context={"request":request}
    )


@account_router.get("/logout")
def logout(request:fastapi.Request):
    """Index page."""
    resp = "<h1>qwe</h1>"
    return template_manager.TemplateResponse(        
        "./index.html",
        context={"request":request}
    )