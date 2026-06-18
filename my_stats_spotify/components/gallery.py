import reflex as rx

from ..style import gallery_style


def gallery() -> rx.Component:
    return rx.box(
        rx.foreach(
            ["/placeholder.png", "/placeholder.png", "/placeholder.png"],
            lambda src: rx.image(src=src),
        ),
        style=gallery_style,
    )
