import reflex as rx

from rxconfig import config
from . import pages, navigation
from .ui.base import base_page
from .translations import LanguageState, translations


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    language = LanguageState.language
    my_child = rx.vstack(
            rx.heading(
                rx.cond(
                    language == "es",
                    translations["es"]["home"]["title"][0],
                    translations["en"]["home"]["title"][0],
                    ),
                    size="9",
            align="center"),
            rx.text(
                rx.cond(
                    language == "es",
                    translations["es"]["home"]["subtitle"][0],
                    translations["en"]["home"]["subtitle"][0],
                    ),
                    size="5",
                align="center",
                padding="0.5em",
            ),
            rx.link(
                rx.button(
                rx.cond(
                    language == "es",
                    translations["es"]["home"]["home_button"][0],
                    translations["en"]["home"]["home_button"][0],
                    ),
                    rx.icon("corner-down-right"),
                          style={
                              "padding": "1.5rem",
                              "borderRadius": "8px",
                              }),
                href=navigation.routes.ABOUT_ROUTE,                
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",            
        )
    return base_page(my_child)


app = rx.App(
    theme=rx.theme(
        accent_color="iris",
        gray_color="slate",
        radius="medium"
    ),
)

app.add_page(index, route="/")
app.add_page(pages.about, route=navigation.routes.ABOUT_ROUTE)
app.add_page(pages.projects, route=navigation.routes.PROJECTS_ROUTE)
app.add_page(pages.contact, route=navigation.routes.CONTACT_ROUTE)