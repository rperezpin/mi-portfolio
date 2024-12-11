import reflex as rx

from ..ui.base import base_page
from .. import navigation

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Contact page", size="9"),
            rx.text(
                "Here you can contact me!",
                size="5",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    return base_page(my_child)