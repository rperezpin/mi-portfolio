"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from . import pages, navigation
from .ui.base import base_page


class State(rx.State):
    """The app state."""



def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("This will be my portfolio", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our about page!"),
                href="/about",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    return base_page(my_child)


app = rx.App()
app.add_page(index)