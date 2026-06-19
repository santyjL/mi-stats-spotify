import reflex as rx

from ..components.footer import footer, separador
from ..components.hero import hero


def mi_top_artistas() -> rx.Component:
    return rx.box(
        hero(),
        separador(),
        footer(),
    )
