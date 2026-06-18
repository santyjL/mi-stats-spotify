import reflex as rx

from ..style import seo_style


def seo(title: str = "Sitio", description: str = "") -> rx.Component:
    return rx.fragment(
        rx.el.title(title),
        rx.el.meta(name="description", content=description),
        rx.box(style=seo_style),
    )
