import reflex as rx

from ..routers import ROUTES
from ..states.logic import StateSpotify
from ..style import (
    Colors,
    footer_brand_text_style,
    footer_divider_style,
    footer_heading_style,
    footer_link_style,
    footer_social_style,
    footer_style,
)


def separador() -> rx.Component:
    return rx.box(
        padding="150px 1px",
    )


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="3"),
        href=href,
        style=footer_link_style,
    )


def footer_items_estadisticas() -> rx.Component:
    return rx.flex(
        rx.heading("ESTADÍSTICAS", size="4", weight="bold", as_="h3", style=footer_heading_style),
        footer_item("Mi Perfil", ROUTES["mi_perfil"]),
        footer_item("Top Artistas", ROUTES["mi_top_artistas"]),
        footer_item("Top Canciones", ROUTES["top_canciones"]),
        footer_item("Historial", ROUTES["historial"]),
        footer_item("Top Álbumes", ROUTES["albumes"]),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_navegacion() -> rx.Component:
    return rx.flex(
        rx.heading("NAVEGACIÓN", size="4", weight="bold", as_="h3", style=footer_heading_style),
        footer_item("Inicio", ROUTES["home"]),
        footer_item("Quién Soy Yo", ROUTES["mi_perfil"]),
        footer_item("Mis Favoritas", ROUTES["top_canciones"]),
        footer_item("Últimas Reproducciones", ROUTES["historial"]),
        footer_item("Mis Álbumes", ROUTES["albumes"]),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(label: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(label, weight="bold"),
        href=href,
        is_external=True,
        style=footer_social_style,
    )


def socials() -> rx.Component:
    return rx.flex(
        social_link("Spotify", "https://open.spotify.com/user/buxb6y049i1f4w77k8gevdurm"),
        social_link("GitHub", "https://github.com/santyjL"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src=StateSpotify.imagen_perfil,
                            width="2.25em",
                            height="2.25em",
                            border_radius="50%",
                            border=f"2px solid {Colors.WHITE.value}",
                            fallback="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_White.png",
                        ),
                        rx.heading("My Stats Spotify", size="7", weight="bold", color=Colors.WHITE.value),
                        align_items="center",
                    ),
                    rx.text(
                        "© 2026 My Stats Spotify · Al estilo de SantyjL",
                        size="3",
                        white_space="nowrap",
                        style=footer_brand_text_style,
                    ),
                    spacing="4",
                    align_items="center",
                ),
                footer_items_estadisticas(),
                footer_items_navegacion(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(style=footer_divider_style),
            rx.hstack(
                rx.hstack(
                    footer_item("Inicio", ROUTES["home"]),
                    footer_item("Mi Perfil", ROUTES["mi_perfil"]),
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
                flex_direction=["column", "column", "row"],
                align="center",
            ),
            spacing="5",
            width="100%",
            max_width="1200px",
            margin="0 auto",
        ),
        style=footer_style,
    )
