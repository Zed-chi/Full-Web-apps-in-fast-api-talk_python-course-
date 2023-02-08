from environs import Env
from starlette.templating import Jinja2Templates


env = Env()
env.read_env()

HTML_DIR = env.str("HTML_DIR", "templates")
ASSETS_DIR = env.str("ASSETS_DIR", "assets")

template_manager = Jinja2Templates(directory=HTML_DIR)
