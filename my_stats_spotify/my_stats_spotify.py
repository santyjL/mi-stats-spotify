import reflex as rx

from .pages.home import home
from .routers import ROUTES
from .states.logic import StateSpotify


app = rx.App()
app.add_page(home, route=ROUTES["home"], on_load=StateSpotify.cargar_datos)

