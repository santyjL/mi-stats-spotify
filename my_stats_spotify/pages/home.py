import reflex as rx

from ..components.flex_data import flex_data_spotify
from ..components.footer import footer, separador
from ..components.hero import hero
from ..style import main_style, body_cursor


def main() -> rx.Component:
    return rx.box(
        flex_data_spotify(),
        style=main_style
    )

def home() -> rx.Component:
    return rx.box(
        hero(),
        main(),
        separador(),
        footer(),
        style=body_cursor
    )
