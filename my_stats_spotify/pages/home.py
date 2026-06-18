import reflex as rx

from ..components.hero import hero
from ..components.footer import footer


def home() -> rx.Component:
    return rx.box(
        hero(),
        footer(),
    )
