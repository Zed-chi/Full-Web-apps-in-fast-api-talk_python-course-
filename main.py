import fastapi
import uvicorn
from settings import template_manager, ASSETS_DIR
from starlette.staticfiles import StaticFiles
from views import account, home, packages


app = fastapi.FastAPI()
app.mount("/static", app=StaticFiles(directory=ASSETS_DIR))
app.include_router(account.account_router)
app.include_router(home.home_router)
app.include_router(packages.packages_router)    


if __name__ == "__main__":
    uvicorn.run(app)
