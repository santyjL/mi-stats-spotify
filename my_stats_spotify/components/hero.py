import reflex as rx

from ..style import hero_style


def hero() -> rx.Component:
    return rx.box(
        rx.heading("Bienvenido", size="9"),
        rx.text("Subtitulo del hero"),
        style=hero_style,
    )
