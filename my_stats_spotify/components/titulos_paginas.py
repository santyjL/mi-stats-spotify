import reflex as rx
from ..style import pagina_titulo_style

def pagina_titulo (titulo:str) -> rx.Component:
    return rx.center(
        rx.text(
            titulo,
            style= pagina_titulo_style
            
        )
    )