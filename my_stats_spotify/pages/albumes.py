import reflex as rx

from ..components.footer import footer, separador
from ..components.hero import hero
from ..states.logic import AlbumItem, StateSpotify
from ..style import (
    album_artista_style,
    album_card_style,
    album_cover_style,
    album_nombre_link_style,
    albumes_grid_style,
    body_cursor
)


def album_card(album: AlbumItem) -> rx.Component:
    return rx.flex(
        rx.avatar(
            src=album["image_url"],
            fallback=album["nombre"],
            style=album_cover_style,
            on_click=rx.redirect(
                path=album["spotify_url"],
                is_external=True
            )
        ),
        rx.link(
            album["nombre"],
            href=album["spotify_url"],
            is_external=True,
            style=album_nombre_link_style,
        ),
        rx.text(
            album["artista"],
            style=album_artista_style,
        ),
        style=album_card_style,
        width=["100%", "calc(50% - 0.75rem)", "calc(33.333% - 1rem)"],
        align="center",
    )


def top_albumes() -> rx.Component:
    return rx.flex(
        rx.foreach(
            StateSpotify.albumes_items,
            album_card,
        ),
        style=albumes_grid_style,
        flex_wrap="wrap",
    )


def albumes() -> rx.Component:
    return rx.box(
        hero(),
        top_albumes(),
        separador(),
        footer(),
        style=body_cursor
    )
