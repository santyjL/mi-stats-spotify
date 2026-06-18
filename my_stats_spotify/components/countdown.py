import reflex as rx

from ..style import countdown_style


def countdown() -> rx.Component:
    return rx.box(
        rx.text("00 : 00 : 00 : 00"),
        style=countdown_style,
    )
