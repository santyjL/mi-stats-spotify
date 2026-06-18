import reflex as rx

from ..style import texts_style


def texts(content: str = "Texto") -> rx.Component:
    return rx.text(content, style=texts_style)
