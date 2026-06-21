import reflex as rx

from .pages.home import home
from .pages.albumes import albumes
from .pages.historial import historial
from .pages.mi_perfil import mi_perfil
from .pages.mi_top_artistas import mi_top_artistas
from .pages.top_canciones import top_canciones
from .routers import Route
from .states.logic import StateSpotify


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Bitcount+Grid+Double:wght@100..900&display=swap",
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap"
        ]
)
app.add_page(home, route=Route.HOME.value, on_load=StateSpotify.cargar_datos)
app.add_page(albumes, route=Route.ALBUMES.value, on_load=StateSpotify.cargar_datos)
app.add_page(historial, route=Route.HISTORIAL.value, on_load=StateSpotify.cargar_datos)
app.add_page(mi_perfil, route=Route.MI_PERFIL.value, on_load=StateSpotify.cargar_datos)
app.add_page(mi_top_artistas, route=Route.MI_TOP_ARTISTAS.value, on_load=StateSpotify.cargar_datos)
app.add_page(top_canciones, route=Route.TOP_CANCIONES.value, on_load=StateSpotify.cargar_datos)

