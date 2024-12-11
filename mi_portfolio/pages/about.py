import reflex as rx

from ..ui.base import base_page
from .. import navigation

@rx.page(route=navigation.routes.ABOUT_ROUTE)
def about() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Something about me", size="9"),
            rx.text(
                "My first about page!",
                size="5",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    return base_page(my_child)