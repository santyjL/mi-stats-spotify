import reflex as rx

from ..style import buttons_style


def buttons(label: str = "Click", href: str = "#") -> rx.Component:
    return rx.link(
        rx.box(label, style=buttons_style),
        href=href,
    )
