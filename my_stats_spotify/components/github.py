import reflex as rx

from ..states.logic import StateGithub
from ..style import github_style


def github() -> rx.Component:
    return rx.box(
        rx.heading("GitHub"),
        rx.foreach(StateGithub.repos, lambda r: rx.text(r)),
        style=github_style,
    )
