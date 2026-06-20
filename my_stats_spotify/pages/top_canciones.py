import reflex as rx

from ..components.footer import footer, separador
from ..components.hero import hero
from ..states.logic import CancionTopItem, StateSpotify
from ..style import (
    top_canciones_artista_style,
    top_canciones_cover_style,
    top_canciones_list_style,
    top_canciones_nombre_style,
    top_canciones_num_style,
    top_canciones_row_style,
)


def cancion_row(cancion: CancionTopItem) -> rx.Component:
    return rx.hstack(
        rx.text(
            cancion["num"],
            style=top_canciones_num_style,
        ),
        rx.avatar(
            src=cancion["image_url"],
            fallback=cancion["nombre"],
            style=top_canciones_cover_style,
        ),
        rx.text(
            cancion["nombre"],
            style=top_canciones_nombre_style,
        ),
        rx.text(
            cancion["artista"],
            style=top_canciones_artista_style,
        ),
        style=top_canciones_row_style,
        width="100%",
    )


def top_canciones_lista() -> rx.Component:
    return rx.flex(
        rx.foreach(
            StateSpotify.top_canciones_items,
            cancion_row,
        ),
        style=top_canciones_list_style,
    )


def top_canciones() -> rx.Component:
    return rx.box(
        hero(),
        top_canciones_lista(),
        separador(),
        footer(),
    )
