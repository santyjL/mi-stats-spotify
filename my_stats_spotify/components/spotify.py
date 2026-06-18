import reflex as rx

from ..states.logic import StateSpotify
from ..style import spotify_style


def spotify() -> rx.Component:
    return rx.box(
        rx.heading("Spotify"),
        rx.foreach(StateSpotify.tracks, lambda t: rx.text(t)),
        style=spotify_style,
    )
