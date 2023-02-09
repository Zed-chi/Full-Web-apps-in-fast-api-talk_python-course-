from fastapi import APIRouter, Request
from settings import template_manager
from view_data.account import AccountViewData, AccountLoginViewData, AccountRegisterViewData

account_router = APIRouter(prefix="/account")


@account_router.get("/")
def account(request:Request):
    """Index page."""
    view_data = AccountViewData(request)
    context = {"request":request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(        
        "./account/account.html",
        context={"request":request}
    )


@account_router.get("/register")
def register(request:Request):
    """Index page."""
    view_data = AccountRegisterViewData(request)
    context = {"request":request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(        
        "./account/register.html",
        context={"request":request}
    )


@account_router.get("/login")
def login(request:Request):
    """Index page."""
    view_data = AccountLoginViewData(request)
    context = {"request":request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(        
        "./account/login.html",
        context={"request":request}
    )


@account_router.get("/logout")
def logout(request:Request):
    """Index page."""
   
    context = {"request":request}

    return template_manager.TemplateResponse(        
        "./account/logout.html",
        context={"request":request}
    )