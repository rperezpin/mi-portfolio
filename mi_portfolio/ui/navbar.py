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
                            src="/logo.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href=navigation.routes.HOME_ROUTE,
                    ),
                    rx.link(
                        rx.heading(
                            "rpi.dev", size="7", weight="bold"
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
                            src="/logo.jpg",
                            width="2em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href=navigation.routes.HOME_ROUTE,
                        ),
                        rx.link(
                            rx.heading(
                                "rpi.dev", size="6", weight="bold"
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
                        rx.menu.item("Home", on_click=navigation.NavState.to_home),
                        rx.menu.item("About", on_click=navigation.NavState.to_about),
                        rx.menu.item("Projects", on_click=navigation.NavState.to_projects),
                        rx.menu.item("Contact", on_click=navigation.NavState.to_contact),
                        rx.divider(),
                        rx.color_mode.button(justify="center"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

