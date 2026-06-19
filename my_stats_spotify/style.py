from enum import Enum


class Colors(Enum):
    PRIMARY = "#1ed760"
    SECONDARY = "#111"
    ACCENT = "#1ed760"
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
    text_wrap="pretty",
    
)

footer_style = dict[str, str](
    background=Colors.PRIMARY.value,
    color=Colors.WHITE.value,
    padding="2rem 1rem",
    width="100%",
)

footer_link_style = dict[str, str](
    color=Colors.WHITE.value,
    text_decoration="none",
    font_size=FontSize.SM.value,
    _hover={"opacity": "0.8"},
)

footer_heading_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.LG.value,
    font_weight="bold",
    text_transform="uppercase",
)

footer_brand_text_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.SM.value,
    font_weight="medium",
)

footer_social_style = dict[str, str](
    color=Colors.WHITE.value,
    font_weight="bold",
    text_decoration="none",
    _hover={"opacity": "0.8"},
)

footer_divider_style = dict[str, str](
    border_color=Colors.WHITE.value,
    opacity="0.35",
    width="100%",
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

main_style = dict[str, str](
    background_color=Colors.SECONDARY.value,
    width="100%"
)

def flex_item(bg, color_texto=Colors.WHITE.value) :
    return dict[str,str](
        flex_basic="0",
        padding="50px",
        align_items="center",
        flex_grow=1,
        background_color=bg,
        border=f"2px solid {Colors.WHITE.value}",
        border_radius="25px",
        color=color_texto
    )

texto_item_flex_style = dict[str,str](
    font_size=FontSize.XL.value, 
    color=Colors.WHITE.value,
    font_weight="bold",
    text_align="center"
)

top_artistas_grid_style = dict[str, str](
    flex_wrap="wrap",
    gap="1.5rem",
    padding="2rem 1rem",
    width="100%",
    max_width="960px",
    margin="0 auto",
    justify_content="center",
)

artista_card_style = dict[str, str](
    align_items="center",
    gap="1rem",
    padding="1rem 1.25rem",
    background_color=Colors.SECONDARY.value,
    border=f"2px solid {Colors.PRIMARY.value}",
    border_radius="1rem",
)

artista_avatar_style = dict[str, str](
    width="72px",
    height="72px",
    border_radius="50%",
    border=f"2px solid {Colors.WHITE.value}",
    flex_shrink="0",
)

artista_nombre_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.LG.value,
    font_weight="bold",
)
