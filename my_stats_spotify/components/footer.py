import reflex as rx

from ..style import footer_style

def separador() -> rx.Component:
    return rx.box(
        padding="150px 1px",
    )

def footer() -> rx.Component:
    return rx.box(
        rx.text("(c) Footer"),
        style=footer_style,
    )
