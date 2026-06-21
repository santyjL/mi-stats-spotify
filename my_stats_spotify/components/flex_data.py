import reflex as rx

from ..style import flex_item, Colors, flex_link_style
from ..routers import Route

cajita1=flex_item(Colors.CELESTE.value)
cajita2=flex_item(Colors.AMARILLO.value)
cajita3=flex_item(Colors.MAGENTA.value)
cajita4=flex_item(Colors.SALMON.value)
cajita5=flex_item(Colors.VERDE_RADIACTIVO.value)

def flex_data_spotify() -> rx.Component:
    return rx.center(
            rx.flex(
                #datos de mi perfil
                rx.box(
                    rx.link(
                        "Mi Perfil",
                        href=Route.MI_PERFIL.value,
                        style=flex_link_style,
                        ),
                    style=cajita1
                ),
                #top mis artistas
                rx.box(
                    rx.link(
                        "Mi Top De Artistas Historico",
                        href=Route.MI_TOP_ARTISTAS.value,
                        style=flex_link_style,
                        ),
                    style=cajita2),
                #top canciones
                rx.box(
                    rx.link(
                        "Mis Canciones Favoritas",
                        href=Route.TOP_CANCIONES.value,
                        style=flex_link_style,
                        ),
                    style=cajita3),
                #historial
                rx.box(
                    rx.link(
                        "Mis Ultimas Reproduccions ",
                        href=Route.HISTORIAL.value,
                        style=flex_link_style,
                        ),
                    style=cajita4),
                #top albumes
                rx.box(
                    rx.link(
                        "Los Albumes Que Mas He Escuchado",
                        href=Route.ALBUMES.value,
                        style=flex_link_style,
                        ),
                    style=cajita5),
            flex_wrap="wrap",
            width="80%",
            align_items="center",
            justify_items="center",
            margin="20px auto",
            gap="25px",
        )
    )