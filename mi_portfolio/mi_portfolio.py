"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from . import pages

from .ui.base import base_page

class State(rx.State):
    """The app state."""



def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(        
        rx.vstack(
            rx.heading("Esto es reflex", size="9"),
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
            min_height="85vh",
        ),
    )



def contact() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("This is how you can contact me", size="9"),
            rx.text(
                "Email, phone and stuff",
                size="5",
            ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )

app = rx.App()
app.add_page(index)
app.add_page(pages.about, route='/about')
app.add_page(contact, route='/contact')