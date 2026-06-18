import reflex as rx

from ..components.navbar import navbar
from ..components.footer import footer


def contact() -> rx.Component:
    return rx.box(
        navbar(),
        rx.heading("Contact"),
        rx.text("Formulario de contacto."),
        footer(),
    )
