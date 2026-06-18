import reflex as rx

from ..style import navbar_style


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Logo"),
            rx.spacer(),
            rx.link("Home", href="/"),
            rx.link("About", href="/about"),
            rx.link("Services", href="/services"),
            rx.link("Contact", href="/contact"),
        ),
        style=navbar_style,
    )
