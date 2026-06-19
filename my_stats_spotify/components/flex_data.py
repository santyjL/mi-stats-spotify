import reflex as rx

from ..style import flex_item, Colors, texto_item_flex_style
from ..routers import ROUTES

cajita1=flex_item(Colors.SUCCESS.value)
cajita2=flex_item(Colors.SUCCESS.value)
cajita3=flex_item(Colors.SUCCESS.value)
cajita4=flex_item(Colors.SUCCESS.value)
cajita5=flex_item(Colors.SUCCESS.value)

def flex_data_spotify(label: str = "Click", href: str = "#") -> rx.Component:
    return rx.center(
            rx.flex(
                #datos de mi perfil
                rx.link(
                    rx.text(
                        "Quien Soy Yo?",
                        style=texto_item_flex_style
                        ),
                    href=ROUTES["mi_perfil"],
                    style=cajita1
                ),
                #top mis artistas
                rx.link(
                    rx.text(
                        "Mi Top De Artistas Historico",
                        style=texto_item_flex_style
                        ),
                    href=ROUTES["mi_top_artistas"],
                    style=cajita2),
                #top canciones
                rx.link(
                    rx.text(
                        "Mis Favoritas(Top 10)",
                        style=texto_item_flex_style
                        ),
                    href=ROUTES["top_canciones"],
                    style=cajita3),
                #historial
                rx.link(
                    rx.text(
                        "Mis Ultimas Reproduccions ",
                        style=texto_item_flex_style
                        ),
                    href=ROUTES["historial"],
                    style=cajita4),
                #top albumes
                rx.link(
                    rx.text(
                        "Los Albumes Que Mas He Escuchado",
                        style=texto_item_flex_style
                        ),
                    href=ROUTES["albumes"],
                    style=cajita5),
            flex_wrap="wrap",
            width="80%",
            align_items="center",
            justify_items="center",
            margin="20px auto",
            gap="25px",
        )
    )