import reflex as rx

from ..states.logic import StateWhatsapp
from ..style import whatsapp_style


def whatsapp() -> rx.Component:
    return rx.link(
        rx.box("WA", style=whatsapp_style),
        href=StateWhatsapp.link,
        is_external=True,
    )
