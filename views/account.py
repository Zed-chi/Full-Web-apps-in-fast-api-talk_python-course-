from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from infrastructure import cookie_auth
from models.account import User
from services import user_service
from settings import template_manager
from view_data.account import (AccountLoginViewData, AccountRegisterViewData,
                               AccountViewData)

account_router = APIRouter(prefix="/account")


@account_router.get("/")
def account(request: Request):
    """Index page."""
    print("=== acc get ===")
    view_data = AccountViewData(request)
    context = {"request": request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(
        "./account/account.html", context=context
    )


@account_router.get("/register")
def register_form(request: Request):
    print("=== reg get ===")
    view_data = AccountRegisterViewData(request)
    context = {"request": request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(
        "./account/register.html", context=context
    )


@account_router.post("/register")
async def register(request: Request):
    """Register page."""
    print("=== acc post ===")
    view_data = AccountRegisterViewData(request)
    await view_data.load()
    if view_data.error:
        return view_data.to_dict()
    account: User = user_service.create_user(
        view_data.name, view_data.email, view_data.password
    )
    response = RedirectResponse("/account/login", 301)
    cookie_auth.set_auth(response, account.pk)
    return response


@account_router.get("/login")
def login(request: Request):
    """Index page."""
    print("=== log get ===")
    view_data = AccountLoginViewData(request)
    context = {"request": request}
    context.update(view_data.to_dict())
    return template_manager.TemplateResponse(
        "./account/login.html", context=context
    )


@account_router.post("/login")
async def login_post(request: Request):
    """Index page."""
    print("=== log post ===")
    view_data = AccountLoginViewData(request)
    await view_data.load()

    if view_data.error:
        return "err"
        return view_data.to_dict()
    user = user_service.login_user(view_data.email, view_data.password)
    if not user:
        return "qwe"
        view_data.error = "Login error"
        return view_data.to_dict()
    resp = RedirectResponse("/account", 301)
    cookie_auth.set_auth(resp, user["pk"])
    return resp


@account_router.get("/logout")
def logout(request: Request):
    """Index page."""
    print("=== lug get ===")
    response = RedirectResponse("/", 301)
    cookie_auth.logout(response)
    return response
