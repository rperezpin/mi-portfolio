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
            rx.heading("Welcome to my place!", size="9", 
            align="center"),
            rx.text(
                "In some way, this is the project about all my projects",                
                size="5",
                align="center"
            ),
            rx.link(
                rx.button("Come here to know a little more about me", rx.icon("corner-down-right")),
                href=navigation.routes.ABOUT_ROUTE,                
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    return base_page(my_child)


app = rx.App()
app.add_page(index)