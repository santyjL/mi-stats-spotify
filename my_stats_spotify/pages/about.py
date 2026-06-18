import reflex as rx

from ..components.navbar import navbar
from ..components.footer import footer


def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.heading("About"),
        rx.text("Acerca de la empresa."),
        footer(),
    )
