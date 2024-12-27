import reflex as rx
from ..ui.base import base_page
from .. import navigation

card_style = {
    "padding":"10px",
    "width":"85%",
    "height":"auto",
    "margin":"auto",
    "marginTop": "10px",
    "marginBottom": "10px",
    "border-radius": "10%",
    }
@rx.page(route=navigation.routes.PROJECTS_ROUTE)
def projects() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Here come everything I've done", size="9", align="center"),
            rx.text(
                "Look at this",
                size="5",
                align="center",
            ),
            rx.grid(
                rx.card(
                        rx.inset(
                            rx.image(
                                src="/logo.jpg",
                                style=card_style,
                            ),
                            side="top",
                            pb="current",
                        ),
                        rx.text(
                            f"Card 1",
                        ),
                    ),
                    rx.card(
                        rx.inset(
                            rx.image(
                                src="/logo.jpg",
                                style=card_style,
                            ),
                            side="top",
                            pb="current",
                        ),
                        rx.text(
                            f"Card 12",
                        ),
                    ),
                gap="1rem",
                grid_template_columns=[
                    "1fr",
                    "repeat(2, 1fr)",
                    "repeat(2, 1fr)",
                    "repeat(3, 1fr)",
                    "repeat(4, 1fr)",
                ],
                width="85%",
            ),
            justify="center",
            align="center",
            marginTop="5rem",
        )
    )
