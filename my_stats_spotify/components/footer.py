import reflex as rx

from ..style import footer_style


def footer() -> rx.Component:
    return rx.box(
        rx.text("(c) Footer"),
        style=footer_style,
    )
