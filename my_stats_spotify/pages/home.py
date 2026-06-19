import reflex as rx

from ..components.flex_data import flex_data_spotify
from ..components.footer import footer
from ..components.hero import hero
from ..style import main_style


def main() -> rx.Component:
    return rx.box(
        flex_data_spotify(),
        style=main_style
    )

def home() -> rx.Component:
    return rx.box(
        hero(),
        main(),
        footer(),
    )
