from enum import Enum


class Colors(Enum):
    PRIMARY = "#0f0f10"
    SECONDARY = "#1f1f23"
    ACCENT = "#00d4ff"
    SUCCESS = "#22c55e"
    WARNING = "#f59e0b"
    DANGER = "#ef4444"
    WHITE = "#ffffff"
    BLACK = "#000000"


class FontSize(Enum):
    XS = "0.75rem"
    SM = "0.875rem"
    MD = "1rem"
    LG = "1.25rem"
    XL = "1.5rem"
    XXL = "2rem"
    DISPLAY = "3rem"


hero_style = dict[str, str](
    background=Colors.SECONDARY.value,
    color=Colors.WHITE.value,
    padding="4rem 1rem",
    text_align="center",
)

footer_style = dict[str, str](
    background=Colors.PRIMARY.value,
    color=Colors.WHITE.value,
    padding="2rem 1rem",
    text_align="center",
)

buttons_style = dict[str, str](
    background=Colors.ACCENT.value,
    color=Colors.WHITE.value,
    padding="0.75rem 1.5rem",
    border_radius="0.5rem",
    cursor="pointer",
)

texts_style = dict[str, str](
    color=Colors.BLACK.value,
    font_size=FontSize.MD.value,
)

spotify_style = dict[str, str](
    padding="1rem",
)

countdown_style = dict[str, str](
    padding="2rem",
    text_align="center",
    color=Colors.ACCENT.value,
    font_size=FontSize.XXL.value,
)
