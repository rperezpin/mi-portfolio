import reflex as rx
from .. import navigation
from ..translations import translations
from ..translations import translations, LanguageState

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
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
                    navbar_link(
                        rx.fragment(
                        rx.cond(
                            LanguageState.language == "es",
                            rx.text(translations["es"]["navbar"]["headers"][0]),  
                            rx.text(translations["en"]["navbar"]["headers"][0]),
                            ), navigation.routes.HOME_ROUTE),
                            ),
                    navbar_link(
                        rx.fragment(
                        rx.cond(
                            LanguageState.language == "es",
                            rx.text(translations["es"]["navbar"]["headers"][1]), 
                            rx.text(translations["en"]["navbar"]["headers"][1]),
                            ), navigation.routes.ABOUT_ROUTE),
                            ),
                    navbar_link(
                        rx.fragment(
                        rx.cond(
                            LanguageState.language == "es",
                            rx.text(translations["es"]["navbar"]["headers"][2]),  
                            rx.text(translations["en"]["navbar"]["headers"][2]),
                            ), navigation.routes.PROJECTS_ROUTE),
                            ),
                    navbar_link(
                        rx.cond(
                            LanguageState.language == "es",
                            rx.text(translations["es"]["navbar"]["headers"][3]), 
                            rx.text(translations["en"]["navbar"]["headers"][3]),
                            ), navigation.routes.CONTACT_ROUTE),
                    spacing="5",
                ),
                rx.button(
                    rx.cond(
                        LanguageState.language == "es",
                        rx.text(translations["es"]["navbar"]["button"][0]),                        
                        rx.text(translations["en"]["navbar"]["button"][0]),
                    ),
                    rx.cond(
                        LanguageState.language == "es",
                        rx.image(src="/english.png",
                                 max_width="20px"),
                        rx.image(src="/spanish.png",
                                 max_width="20px"),
                        ),
                    on_click=LanguageState.change_language,
                ),
                justify="center",
                spacing="6",
                align_items="center",
            ),
        ),
        rx.mobile_only(
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
                            rx.link(
                                rx.cond(
                                    LanguageState.language == "es",
                                    rx.text(translations["es"]["navbar"]["headers"][0]),   
                                    rx.text(translations["en"]["navbar"]["headers"][0]),
                                    ), href=navigation.routes.HOME_ROUTE, width="100%")
                        ),
                        rx.menu.item(
                            rx.link(
                                rx.cond(
                                    LanguageState.language == "es",
                                    rx.text(translations["es"]["navbar"]["headers"][1]),
                                    rx.text(translations["en"]["navbar"]["headers"][1]),
                                    ), href=navigation.routes.ABOUT_ROUTE, width="100%")
                        ),
                        rx.menu.item(
                            rx.link(
                                rx.cond(
                                    LanguageState.language == "es",
                                    rx.text(translations["es"]["navbar"]["headers"][2]),
                                    rx.text(translations["en"]["navbar"]["headers"][2]),
                                    ), href=navigation.routes.PROJECTS_ROUTE, width="100%")
                        ),
                        rx.menu.item(
                            rx.link(
                                rx.cond(
                                    LanguageState.language == "es",
                                    rx.text(translations["es"]["navbar"]["headers"][3]),                        
                                    rx.text(translations["en"]["navbar"]["headers"][3]),
                                ), href=navigation.routes.CONTACT_ROUTE, width="100%")
                        ),
                        rx.divider(),
                        rx.color_mode.button(justify="center"),
                        rx.button(
                            rx.cond(
                                LanguageState.language == "es",
                                rx.image(src="/english.png",
                                         max_width="20px"),
                                rx.image(src="/spanish.png",
                                         max_width="20px"),
                                ),
                            on_click=LanguageState.change_language,
                        ),
                    ),
                    justify="start",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color_mode_cond(
            light="#e3e6f6",  # Color para el modo claro
            dark="gray_color",
        ),
        padding="0.5em",
        width="100%",
    )

