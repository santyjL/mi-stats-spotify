import reflex as rx

from ..states.logic import StateYoutube
from ..style import youtube_style


def youtube() -> rx.Component:
    return rx.box(
        rx.heading("YouTube"),
        rx.foreach(StateYoutube.videos, lambda v: rx.text(v)),
        style=youtube_style,
    )
