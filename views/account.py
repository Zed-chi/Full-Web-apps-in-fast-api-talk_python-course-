from fastapi import APIRouter, Request
from settings import template_manager


account_router = APIRouter(prefix="/account")


@account_router.get("/")
def account(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./account/account.html",
        context={"request":request}
    )


@account_router.get("/register")
def register(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./account/register.html",
        context={"request":request}
    )


@account_router.get("/login")
def login(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./account/login.html",
        context={"request":request}
    )


@account_router.get("/logout")
def logout(request:Request):
    """Index page."""
    return template_manager.TemplateResponse(        
        "./account/logout.html",
        context={"request":request}
    )