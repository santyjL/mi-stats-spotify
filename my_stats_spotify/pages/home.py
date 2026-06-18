import reflex as rx

from ..components.navbar import navbar
from ..components.hero import hero
from ..components.countdown import countdown
from ..components.footer import footer


def home() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        countdown(),
        footer(),
    )
