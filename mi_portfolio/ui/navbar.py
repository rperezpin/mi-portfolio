import reflex as rx
from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src=rx.color_mode_cond(
                                light="/logo_azul1.png",
                                dark="/logo_blanco.png",
                            ),
                            width="7em",
                            height="auto",
                        ),
                        href=navigation.routes.HOME_ROUTE,
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    navbar_link("Projects", navigation.routes.PROJECTS_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_ROUTE),
                    spacing="5",
                ),
                justify="center",
                spacing="8",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src=rx.color_mode_cond(
                                light="/logo_azul1.png",
                                dark="/logo_blanco.png",
                            ),
                            width="7em",
                            height="auto",
                        ),
                        href=navigation.routes.HOME_ROUTE,
                    ),
                    align_items="center",
                    justify="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            rx.link("Home", href=navigation.routes.HOME_ROUTE, width="100%")
                        ),
                        rx.menu.item(
                            rx.link("About", href=navigation.routes.ABOUT_ROUTE, width="100%")
                        ),
                        rx.menu.item(
                            rx.link("Projects", href=navigation.routes.PROJECTS_ROUTE, width="100%")
                        ),
                        rx.menu.item(
                            rx.link("Contact", href=navigation.routes.CONTACT_ROUTE, width="100%")
                        ),
                        rx.divider(),
                        rx.color_mode.button(justify="center"),
                    ),
                    justify="start",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="0.5em",
        width="100%",
    )

