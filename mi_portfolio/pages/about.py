import reflex as rx
from ..ui.base import base_page
from .. import navigation
from .translations import LanguageState, translations

class TimelineState(rx.State):
    # Estado para controlar qué textos están visibles
    visible_text: str | None = None

    def toggle_text(self, text_id: str):
        """Alterna la visibilidad del texto."""
        self.visible_text = None if self.visible_text == text_id else text_id


def timeline_item(text: str, icon: str, align: str, button_text: str, item_id: str) -> rx.Component:
    """Crea un elemento individual de la línea de tiempo."""
    is_left = align == "left"
    is_visible = TimelineState.visible_text == item_id

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
                            "color": rx.color_mode_cond(light="black", dark="white"),
                        },
                    ),
                    spacing="2",
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
                    "@media (max-width: 768px)": {
                        "maxWidth": "80%",
                        "padding": "1.5rem",
                    },
                    "@media (max-width: 480px)": {
                        "maxWidth": "100%",
                        "padding": "1rem",
                    },
                },
            ),
            justify="start" if is_left else "end",
            align="center",
            width="100%",
            style={
                "paddingRight": "4rem" if is_left else "1rem",
                "paddingLeft": "4rem" if not is_left else "1rem",
            },
        ),
        # Hover card para el botón
        rx.hover_card.root(
            rx.hover_card.trigger(
                rx.button(
                    "",
                    on_click=TimelineState.toggle_text(item_id),
                    style={
                        "borderRadius": "50%",
                        "width": "16px",
                        "height": "16px",
                        "position": "absolute",
                        "left": "50%",
                        "transform": "translateX(-50%)",
                        "backgroundColor": "#3182CE",
                        "border": "4px solid white",
                        "boxShadow": "0 0 0 2px #3182CE",
                        "marginTop": "4em",
                        "marginBottom": "4em",
                    },
                ),
            ),
            rx.hover_card.content(
                    rx.text(
                        button_text,
                        style={"color": "white", 
                               "fontSize": "1rem",
                               "backgroundColor": "#3182CE",
                               "padding": "1rem",
                               "borderRadius": "8px",
                               "boxShadow": "0 4px 6px rgba(0,0,0,0.2)", 
                               },
                    
                ),                
                align="start" if not is_left else "end",
            ),
        ),
        position="relative",
        margin_y="4em",  # Aumentamos el espacio vertical entre items
        width="100%",
    )


@rx.page(route=navigation.routes.ABOUT_ROUTE)
def about() -> rx.Component:
    timeline_items = [
        {
            "text": rx.cond(
                        LanguageState.language == "es",
                        rx.text(translations["es"]["about"]["timeline"][0]),
                        rx.text(translations["en"]["about"]["timeline"][0]),
                    ),
            "icon": "graduation_cap",
            "align": "left",
            "button_text": "Aquí aprendí poco",
            "id": "1"
        },
        {
            "text":  rx.cond(
                        LanguageState.language == "es",
                        rx.text(translations["es"]["about"]["timeline"][1]),
                        rx.text(translations["en"]["about"]["timeline"][1]),
                    ),
            "icon": "laptop",
            "align": "right",
            "button_text": "Aquí un poco más",
            "id": "2"
        },
        {
            "text":  rx.cond(
                        LanguageState.language == "es",
                        rx.text(translations["es"]["about"]["timeline"][2]),
                        rx.text(translations["en"]["about"]["timeline"][2]),
                    ),
            "icon": "rocket",
            "align": "left",
            "button_text": "Aquí casi na",
            "id": "3"
        },
        {
            "text":  rx.cond(
                        LanguageState.language == "es",
                        rx.text(translations["es"]["about"]["timeline"][3]),
                        rx.text(translations["en"]["about"]["timeline"][3]),
                    ),
            "icon": "wrench",
            "align": "right",
            "button_text": "Aquí soy un hacker",
            "id": "4"
        },
    ]

    return base_page(
        rx.box(
            rx.vstack(
                # Línea vertical central
                rx.box(
                    style={
                        "position": "absolute",
                        "top": "0",
                        "bottom": "0",
                        "left": "50%",
                        "width": "4px",
                        "backgroundColor": "#3182CE",
                        "transform": "translateX(-50%)",
                        "marginTop": "4rem",
                        "marginBottom": "8rem"
                    }
                ),            
                # Items de la línea temporal
                *[
                    timeline_item(
                        text=item["text"],
                        icon=item["icon"],
                        align=item["align"],
                        button_text=item["button_text"],
                        item_id=item["id"],
                    )
                    for item in timeline_items
                ],

              rx.box(
                  rx.link(                      
                      rx.button("Let's see some of my projects", 
                          rx.icon("corner-down-right"),
                          style={
                              "position": "absolute",
                              "left": "50%",
                              "transform": "translateX(-50%)",
                              "padding": "1.5rem",
                              "borderRadius": "8px",
                              }
                              ),
                              href=navigation.routes.PROJECTS_ROUTE,
                        ),
                        margin_top="4rem",
                        margin_bottom="8rem",
                    ),
                position="relative",
                width="100%",
                max_width="800px",
                margin="auto",
                spacing="4",
            ),
            style={
                "minHeight": "85vh",
            },
          
        ),
    )