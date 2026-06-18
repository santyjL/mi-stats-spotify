import reflex as rx

from ..style import faq_style


def faq() -> rx.Component:
    return rx.box(
        rx.heading("Preguntas frecuentes"),
        rx.text("Pregunta 1?"),
        rx.text("Respuesta 1."),
        style=faq_style,
    )
