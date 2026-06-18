import reflex as rx

from ..components.navbar import navbar
from ..components.footer import footer


def services() -> rx.Component:
    return rx.box(
        navbar(),
        rx.heading("Services"),
        rx.text("Nuestros servicios."),
        footer(),
    )
