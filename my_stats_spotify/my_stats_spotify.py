import reflex as rx

from .pages.home import home
from .routers import ROUTES


app = rx.App()
app.add_page(home, route=ROUTES["home"])

