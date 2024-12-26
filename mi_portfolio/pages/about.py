import reflex as rx
from ..ui.base import base_page
from .. import navigation


class ClickState(rx.State):
    # Diccionario para almacenar el estado de visualización de cada texto
    visible_texts: dict[str, str] = {}

    def toggle_text(self, text_id: str):
        """Toggle la visibilidad de un texto específico."""
        current = self.visible_texts.get(text_id, "none")
        self.visible_texts[text_id] = "none" if current == "block" else "block"


@rx.page(route=navigation.routes.ABOUT_ROUTE)
def about() -> rx.Component:
    return base_page(
        rx.box(
            rx.vstack(
                rx.box(
                    style={
                        "position": "absolute",
                        "top": "0",
                        "bottom": "0",
                        "left": "50%",
                        "width": "4px",
                        "backgroundColor": "#3182CE",
                        "transform": "translateX(-50%)",
                    }
                ),
                create_timeline_item(
                    text="Comencé a estudiar programación en 2020.",
                    icon="graduation_cap",
                    align="left",
                    button_text="Aquí aprendí poco",
                    text_id="text1",  # Identificador único
                ),
                create_timeline_item(
                    text="Desarrollé mi primera aplicación en 2021.",
                    icon="laptop",
                    align="right",
                    button_text="Aquí un poco más",
                    text_id="text2",  # Identificador único
                ),
                create_timeline_item(
                    text="Trabajé en proyectos freelance en 2022.",
                    icon="rocket",
                    align="left",
                    button_text="Aquí casi na",
                    text_id="text3",  # Identificador único
                ),
                create_timeline_item(
                    text="Estoy mejorando mis habilidades como full-stack.",
                    icon="wrench",
                    align="right",
                    button_text="Aquí soy un hacker",
                    text_id="text4",  # Identificador único
                ),
                spacing="6",
                position="relative",
                style={"width": "100%", "maxWidth": "800px", "margin": "auto"},
            ),
            style={
                "minHeight": "100vh",
                "marginTop": "8rem",
            },
        ),    
    )


def create_timeline_item(text: str, icon: str, align: str, button_text: str, text_id: str) -> rx.Component:
    is_left = align == "left"

    return rx.box(
        rx.hstack(
            rx.box(
                rx.hstack(
                    rx.icon(icon, size=55),
                    rx.text(
                        text,
                        style={
                            "fontSize": "1rem",
                            "lineHeight": "1.5",
                            "color": rx.color_mode_cond(
                                light="black",
                                dark="white",
                            ),
                        },
                    ),
                    spacing="4",
                ),
                style={
                    "backgroundColor": rx.color_mode_cond(
                        light="#f7f7f7",
                        dark="#2d3748",
                    ),
                    "padding": "2rem",
                    "borderRadius": "8px",
                    "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
                    "maxWidth": "60%",
                    "textAlign": "left" if is_left else "right",
                    "@media (max-width: 768px)": {
                        "maxWidth": "80%",
                        "padding": "1.5rem",
                        "marginBottom": "2rem",
                    },
                    "@media (max-width: 480px)": {
                        "maxWidth": "100%",
                        "padding": "1rem",
                    },
                },
            ),
            justify="start" if is_left else "end",
            width="100%",
            style={
                "paddingRight": "7rem" if is_left else "0",
                "paddingLeft": "7rem" if not is_left else "0",
                "@media (max-width: 768px)": {
                    "paddingRight": "8rem" if is_left else "1rem",
                    "paddingLeft": "8rem" if not is_left else "1rem",
                    "width":"80%",
                },
                "@media (max-width: 480px)": {
                    "paddingRight": "1rem" if is_left else "0.5rem",
                    "paddingLeft": "1rem" if not is_left else "0.5rem",
                    "width":"100%",
                },
            },
        ),
        rx.desktop_only(
            rx.hover_card.root(
                rx.hover_card.trigger(
                    rx.box(
                        style={
                            "position": "absolute",
                            "left": "50%",
                            "top": "50%",                 
                            "width": "16px",
                            "height": "16px",
                            "borderRadius": "50%",
                            "backgroundColor": "#3182CE",
                            "border": "4px solid white",
                            "transform": "translate(-50%, -50%)",
                            "boxShadow": "0 0 0 2px #3182CE",
                        },
                    ),
                ),
                rx.hover_card.content(
                    rx.box(
                        rx.text(
                            f"{button_text}.",
                            style={"color": "white", "fontSize": "1rem", "lineHeight": "1.5"},
                        ),
                        style={
                            "backgroundColor": "#3182CE",
                            "padding": "1rem",
                            "borderRadius": "8px",
                            "boxShadow": "0 4px 6px rgba(0,0,0,0.2)",
                        },
                    ),
                    style={
                        "left": "5%" if is_left else "auto",
                        "right": "102%" if not is_left else "auto",
                        "top": "-80px",
                        "@media (max-width: 768px)": {
                            "display": "none",
                        },
                        "@media (max-width: 480px)": {
                            "display": "none",
                        },
                    },
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.button("",
                style={
                    "position": "absolute",
                    "left": "50%",
                    "top": "100%",                 
                    "width": "16px",
                    "height": "16px",
                    "borderRadius": "50%",
                    "backgroundColor": "#3182CE",
                    "border": "4px solid white",
                    "transform": "translate(-50%, -50%)",
                    "boxShadow": "0 0 0 2px #3182CE",
                },
                on_click=lambda tid=text_id: ClickState.toggle_text(tid),
            ),
            rx.box(
                rx.text(
                    f"{button_text}.",
                    style={"color": "white", "fontSize": "1rem", "lineHeight": "1.5"},
                ),
                style={
                    "display": ClickState.visible_texts[text_id],                    
                    "transition": "opacity 8s ease, transform 8s ease",  
                    "backgroundColor": "#3182CE",
                    "padding": "1rem",
                    "borderRadius": "8px",
                    "boxShadow": "0 4px 6px rgba(0,0,0,0.2)",
                },
            ),
        ),
        position="relative",
        style={
            "left": "50%",
            "alignItems": "center",
            "transform": "translate(-50%, -50%)",
        },
    )