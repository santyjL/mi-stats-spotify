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

def flex_item(border_color, color_texto=Colors.WHITE.value) :
    return dict[str,str](
        flex_basic="0",
        padding="50px",
        align_items="center",
        flex_grow=1,
        background_color="transparent",
        border_bottom=f"5px solid {border_color}",
        border_top=f"3px solid {border_color}",
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

historial_grid_style = dict[str, str](
    flex_wrap="wrap",
    gap="1.5rem",
    padding="2rem 1rem",
    width="100%",
    max_width="960px",
    margin="0 auto",
    justify_content="center",
)

historial_card_style = dict[str, str](
    align_items="center",
    gap="1rem",
    padding="1rem 1.25rem",
    background_color=Colors.SECONDARY.value,
    border=f"2px solid {Colors.PRIMARY.value}",
    border_radius="1rem",
)

historial_cover_style = dict[str, str](
    width="72px",
    height="72px",
    border_radius="0.5rem",
    border=f"2px solid {Colors.WHITE.value}",
    flex_shrink="0",
)

historial_nombre_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.LG.value,
    font_weight="bold",
)

historial_artista_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.SM.value,
    opacity="0.85",
)

albumes_grid_style = dict[str, str](
    flex_wrap="wrap",
    gap="1.5rem",
    padding="2rem 1rem",
    width="100%",
    max_width="960px",
    margin="0 auto",
    justify_content="center",
)

album_card_style = dict[str, str](
    flex_direction="column",
    align_items="center",
    gap="0.75rem",
    padding="1rem 1.25rem",
    background_color=Colors.SECONDARY.value,
    border=f"2px solid {Colors.PRIMARY.value}",
    border_radius="1rem",
)

album_cover_style = dict[str, str](
    width="140px",
    height="140px",
    border_radius="0.5rem",
    border=f"2px solid {Colors.WHITE.value}",
    flex_shrink="0",
)

album_nombre_link_style = dict[str, str](
    color=Colors.PRIMARY.value,
    font_size=FontSize.LG.value,
    font_weight="bold",
    text_align="center",
    text_decoration="none",
    _hover={"opacity": "0.8"},
)

album_artista_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.SM.value,
    opacity="0.85",
    text_align="center",
)

top_canciones_list_style = dict[str, str](
    flex_direction="column",
    width="80%",
    margin="0 auto",
    padding="2rem 1rem",
)

top_canciones_row_style = dict[str, str](
    align_items="center",
    gap="1.25rem",
    padding="1rem 0",
    border_bottom=f"2px solid {Colors.PRIMARY.value}",
    width="100%",
)

top_canciones_num_style = dict[str, str](
    color=Colors.PRIMARY.value,
    font_size=FontSize.XL.value,
    font_weight="bold",
    min_width="2rem",
    text_align="center",
    flex_shrink="0",
)

top_canciones_cover_style = dict[str, str](
    width="64px",
    height="64px",
    border_radius="0.5rem",
    border=f"2px solid {Colors.WHITE.value}",
    flex_shrink="0",
)

top_canciones_nombre_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.LG.value,
    font_weight="bold",
    flex="1",
    min_width="0",
)

top_canciones_artista_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.SM.value,
    opacity="0.85",
    flex="1",
    min_width="0",
)

top_canciones_reproducciones_style = dict[str, str](
    color=Colors.PRIMARY.value,
    font_size=FontSize.MD.value,
    font_weight="bold",
    min_width="6rem",
    text_align="right",
    flex_shrink="0",
)

mi_perfil_grid_style = dict[str, str](
    gap="1.5rem",
    padding="2rem 1rem",
    width="100%",
    max_width="1200px",
    margin="0 auto",
    align_items="stretch",
    justify_content="center",
)

mi_perfil_columna_style = dict[str, str](
    flex_direction="column",
    gap="1.5rem",
    flex="1",
    min_width="280px",
)

mi_perfil_card_style = dict[str, str](
    flex_direction="column",
    gap="0.75rem",
    padding="1.5rem",
    background_color=Colors.SECONDARY.value,
    border=f"2px solid {Colors.PRIMARY.value}",
    border_radius="1rem",
    width="100%",
)

mi_perfil_card_titulo_style = dict[str, str](
    color=Colors.PRIMARY.value,
    font_size=FontSize.XL.value,
    font_weight="bold",
    text_transform="uppercase",
)

mi_perfil_card_label_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.SM.value,
    font_weight="bold",
    opacity="0.7",
    text_transform="uppercase",
)

mi_perfil_card_valor_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.MD.value,
    font_weight="medium",
)

reproduccion_cover_style = dict[str, str](
    width="96px",
    height="96px",
    border_radius="0.5rem",
    border=f"2px solid {Colors.WHITE.value}",
    flex_shrink="0",
)

reproduccion_nombre_style = dict[str, str](
    color=Colors.PRIMARY.value,
    font_size=FontSize.LG.value,
    font_weight="bold",
    text_decoration="none",
    _hover={"opacity": "0.8"},
)

reproduccion_estado_style = dict[str, str](
    color=Colors.PRIMARY.value,
    font_size=FontSize.SM.value,
    font_weight="bold",
    text_transform="uppercase",
)

artistas_mes_lista_style = dict[str, str](
    flex_direction="column",
    gap="0.75rem",
    width="100%",
    max_height="640px",
    overflow_y="auto",
)

artista_mes_row_style = dict[str, str](
    align_items="center",
    gap="0.75rem",
    padding="0.5rem 0.75rem",
    border_bottom=f"1px solid {Colors.PRIMARY.value}",
    width="100%",
)

artista_mes_avatar_style = dict[str, str](
    width="48px",
    height="48px",
    border_radius="50%",
    border=f"2px solid {Colors.WHITE.value}",
    flex_shrink="0",
)

artista_mes_nombre_style = dict[str, str](
    color=Colors.WHITE.value,
    font_size=FontSize.MD.value,
    font_weight="bold",
)
