import reflex as rx

from .pages.home import home
from .pages.albumes import albumes
from .pages.historial import historial
from .pages.mi_perfil import mi_perfil
from .pages.mi_top_artistas import mi_top_artistas
from .pages.top_canciones import top_canciones
from .routers import ROUTES
from .states.logic import StateSpotify


app = rx.App()
app.add_page(home, route=ROUTES["home"], on_load=StateSpotify.cargar_datos)
app.add_page(albumes, route=ROUTES["albumes"], on_load=StateSpotify.cargar_datos)
app.add_page(historial, route=ROUTES["historial"], on_load=StateSpotify.cargar_datos)
app.add_page(mi_perfil, route=ROUTES["mi_perfil"], on_load=StateSpotify.cargar_datos)
app.add_page(mi_top_artistas, route=ROUTES["mi_top_artistas"], on_load=StateSpotify.cargar_datos)
app.add_page(top_canciones, route=ROUTES["top_canciones"], on_load=StateSpotify.cargar_datos)

