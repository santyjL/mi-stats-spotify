import reflex as rx

from ..components.footer import footer, separador
from ..components.hero import hero
from ..states.logic import HistorialItem, StateSpotify
from ..components.titulos_paginas import pagina_titulo

from ..style import (
    historial_artista_style,
    historial_card_style,
    historial_cover_style,
    historial_grid_style,
    historial_nombre_style,
    body_cursor
)


def historial_card(cancion: HistorialItem) -> rx.Component:
    return rx.flex(
        rx.avatar(
            src=cancion["image_url"],
            fallback=cancion["name"],
            style=historial_cover_style,
        ),
        rx.vstack(
            rx.heading(
                cancion["name"],
                size="5",
                style=historial_nombre_style,
            ),
            rx.text(cancion["album_name"]),
            rx.text(
                cancion["artist"],
                style=historial_artista_style,
            ),
            spacing="1",
            align="start",
        ),
        style=historial_card_style,
        width=["100%", "calc(50% - 0.75rem)"],
        align="center",
    )


def ultimas_reproducciones() -> rx.Component:
    return rx.flex(
        rx.foreach(
            StateSpotify.historial_items,
            historial_card,
        ),
        style=historial_grid_style,
        flex_wrap="wrap",
    )


def historial() -> rx.Component:
    return rx.box(
        hero(),
        pagina_titulo("MI HISTORIAL DE REPRODUCCION"),
        ultimas_reproducciones(),
        separador(),
        footer(),
        style=body_cursor
    )
