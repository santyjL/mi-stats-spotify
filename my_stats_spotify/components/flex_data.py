import reflex as rx

from ..style import flex_item, Colors

cajita1=flex_item(Colors.SUCCESS.value)
cajita2=flex_item(Colors.SUCCESS.value)
cajita3=flex_item(Colors.SUCCESS.value)
cajita4=flex_item(Colors.SUCCESS.value)
cajita5=flex_item(Colors.SUCCESS.value)
cajita6=flex_item(Colors.SUCCESS.value)

def flex_data_spotify(label: str = "Click", href: str = "#") -> rx.Component:
    return rx.center(
            rx.flex(
                rx.box(style=cajita1),
                rx.box(style=cajita2),
                rx.box(style=cajita3),
                rx.box(style=cajita4),
                rx.box(style=cajita5),
                rx.box(style=cajita6),
            flex_wrap="wrap",
            width="90%",
            align_items="center",
            justify_items="center",
            margin="20px auto",
            gap="10px",
        )
    )