import reflex as rx

from ..states.logic import StateWeather
from ..style import weather_style


def weather() -> rx.Component:
    return rx.box(
        rx.heading("Clima"),
        rx.text(StateWeather.temperature),
        rx.text(StateWeather.description),
        style=weather_style,
    )
