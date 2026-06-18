import reflex as rx

from ..components.hero import hero
from ..components.countdown import countdown
from ..components.footer import footer


def home() -> rx.Component:
    return rx.box(
        hero(),
        countdown(),
        footer(),
    )
