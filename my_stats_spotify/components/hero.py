
from turtle import position
import reflex as rx
from ..style import hero_style, Colors
from ..services.spotify_api import imagen_perfil

def hero() -> rx.Component:
    return rx.box(
        rx.center(
            rx.image(
                src=imagen_perfil,
                border_radius="50%",
                border=f"2px solid {Colors.WHITE.value}",
                margin="20px",
                width="256px",
                height="256px"
            ),
        ),
        rx.heading("COMIENZA A ESCUCHAR MUSICA DE FORMA DIFERENTE",
                    size="9",
                    text_align="center",
                    text_wrap="balance",
                    text_shadow=f"0 0 40px {Colors.ACCENT.value}"),
        rx.text("Al estilo de SantyjL", text_align="center"),
        style=hero_style,
    )
