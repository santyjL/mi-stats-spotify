import reflex as rx

from ..components.footer import footer, separador
from ..components.hero import hero
from ..states.logic import ArtistaItem, StateSpotify
from ..components.titulos_paginas import pagina_titulo
from ..style import (
    artista_avatar_style,
    artista_card_style,
    artista_nombre_style,
    top_artistas_grid_style,
    body_cursor
)


def artista_card(artista: ArtistaItem) -> rx.Component:
    return rx.flex(
        rx.avatar(
            src=artista["image_url"],
            fallback=artista["name"],
            style=artista_avatar_style,
        ),
        rx.heading(
            artista["name"],
            size="5",
            style=artista_nombre_style,
        ),
        style=artista_card_style,
        width=["100%", "calc(50% - 0.75rem)"],
        align="center",
    )


def top_de_artistas() -> rx.Component:
    return rx.flex(
        rx.foreach(
            StateSpotify.artistas_items,
            artista_card,
        ),
        style=top_artistas_grid_style,
        flex_wrap="wrap",
    )


def mi_top_artistas() -> rx.Component:
    return rx.box(
        hero(),
        pagina_titulo("MI TOP DE ARTISTAS"),
        top_de_artistas(),
        separador(),
        footer(),
        style=body_cursor
    )
