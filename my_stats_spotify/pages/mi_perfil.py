import reflex as rx

from ..components.footer import footer, separador
from ..components.hero import hero
from ..states.logic import ArtistaItem, StateSpotify
from ..style import (
    artista_mes_avatar_style,
    artista_mes_nombre_style,
    artista_mes_row_style,
    artistas_mes_lista_style,
    mi_perfil_card_label_style,
    mi_perfil_card_style,
    mi_perfil_card_titulo_style,
    mi_perfil_card_valor_style,
    mi_perfil_columna_style,
    mi_perfil_grid_style,
    reproduccion_cover_style,
    reproduccion_estado_style,
    reproduccion_nombre_style,
    body_cursor
)


def _campo_perfil(label: str, valor: rx.Var | str) -> rx.Component:
    return rx.flex(
        rx.text(label, style=mi_perfil_card_label_style),
        rx.text(valor, style=mi_perfil_card_valor_style),
        flex_direction="column",
        gap="0.15rem",
        width="100%",
    )


def perfil_info_card() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Quién soy yo",
            size="6",
            style=mi_perfil_card_titulo_style,
        ),
        _campo_perfil("Nombre", StateSpotify.display_name),
        _campo_perfil("ID", StateSpotify.user_id),
        _campo_perfil("País", StateSpotify.pais),
        _campo_perfil("Plan", StateSpotify.plan),
        style=mi_perfil_card_style,
    )


def reproduccion_actual_card() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Reproducción actual",
            size="6",
            style=mi_perfil_card_titulo_style,
        ),
        rx.cond(
            StateSpotify.hay_reproduccion,
            rx.hstack(
                rx.avatar(
                    src=StateSpotify.reproduccion_actual_item["image_url"],
                    fallback=StateSpotify.reproduccion_actual_item["nombre"],
                    style=reproduccion_cover_style,
                ),
                rx.vstack(
                    rx.link(
                        StateSpotify.reproduccion_actual_item["nombre"],
                        href=StateSpotify.reproduccion_actual_item["spotify_url"],
                        is_external=True,
                        style=reproduccion_nombre_style,
                    ),
                    rx.text(
                        StateSpotify.reproduccion_actual_item["artista"],
                        style=mi_perfil_card_valor_style,
                    ),
                    rx.text(
                        StateSpotify.reproduccion_actual_item["album"],
                        style=mi_perfil_card_label_style,
                    ),
                    rx.cond(
                        StateSpotify.reproduccion_actual_item["is_playing"],
                        rx.text("▶ Reproduciendo", style=reproduccion_estado_style),
                        rx.text("⏸ En pausa", style=reproduccion_estado_style),
                    ),
                    spacing="1",
                    align="start",
                ),
                spacing="3",
                align="center",
                width="100%",
            ),
            rx.text(
                "No hay reproducción activa en este momento.",
                style=mi_perfil_card_valor_style,
            ),
        ),
        style=mi_perfil_card_style,
    )


def artista_mes_row(artista: ArtistaItem) -> rx.Component:
    return rx.hstack(
        rx.avatar(
            src=artista["image_url"],
            fallback=artista["name"],
            style=artista_mes_avatar_style,
        ),
        rx.text(
            artista["name"],
            style=artista_mes_nombre_style,
        ),
        style=artista_mes_row_style,
    )


def top_artistas_mes_card() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Top artistas del mes",
            size="6",
            style=mi_perfil_card_titulo_style,
        ),
        rx.text(
            "Últimas 4 semanas",
            style=mi_perfil_card_label_style,
        ),
        rx.cond(
            StateSpotify.artistas_mes_items,
            rx.flex(
                rx.foreach(
                    StateSpotify.artistas_mes_items,
                    artista_mes_row,
                ),
                style=artistas_mes_lista_style,
            ),
            rx.text(
                "No se pudieron obtener los artistas del mes.",
                style=mi_perfil_card_valor_style,
            ),
        ),
        style=mi_perfil_card_style,
        height="100%",
    )


def mi_perfil_grid() -> rx.Component:
    return rx.flex(
        rx.flex(
            perfil_info_card(),
            reproduccion_actual_card(),
            style=mi_perfil_columna_style,
        ),
        rx.flex(
            top_artistas_mes_card(),
            style=mi_perfil_columna_style,
        ),
        style=mi_perfil_grid_style,
        flex_direction=["column", "column", "row"],
        flex_wrap="wrap",
    )


def mi_perfil() -> rx.Component:
    return rx.box(
        hero(),
        mi_perfil_grid(),
        separador(),
        footer(),
        style=body_cursor
    )
