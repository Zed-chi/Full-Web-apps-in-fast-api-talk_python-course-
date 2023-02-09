import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from settings import ASSETS_DIR
from views import account, home, packages

app = fastapi.FastAPI()


def main():
    init()
    uvicorn.run(app)


def init():
    app.mount("/static", app=StaticFiles(directory=ASSETS_DIR))
    app.include_router(account.account_router)
    app.include_router(home.home_router)
    app.include_router(packages.packages_router)


if __name__ == "__main__":
    main()
else:
    init()
