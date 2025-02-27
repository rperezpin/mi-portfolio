import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..translations import translations, LanguageState
import time

class TimelineState(rx.State):
    # Estado para controlar qué textos están visibles
    visible_text: str | None = None
    last_clicked: str | None = None  # Nuevo estado para rastrear clics

    def toggle_text(self, text_id: str):
        """Alterna la visibilidad del texto"""
        self.last_clicked = text_id
        self.visible_text = text_id if self.visible_text != text_id else None

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
                    "padding": "1.5rem",
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
        # Replace hover card with a tooltip for mobile compatibility
        rx.tooltip(
            rx.button(
                "",
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
                    "cursor": "pointer",
                    # Ocultar tooltip en móviles
                    "@media (max-width: 768px)": {
                        "display": "none"
                    }
                },
                on_click=TimelineState.toggle_text(item_id),
            ),
            content=button_text,
            background_color="#3182CE",
            color="white",
            border_radius="8px",
            padding="1rem",
            font_size="5em",
            placement="top" if is_left else "bottom",
        ),
        # Versión móvil con clic
        rx.button(
            "",
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
                "cursor": "pointer",
                # Ocultar en desktop
                "@media (min-width: 769px)": {
                    "display": "none"
                }
            },
            on_click=TimelineState.toggle_text(item_id),
        ),
        # Overlay para cerrar al hacer clic fuera
        rx.cond(
            is_visible,
            rx.box(
                style={
                    "position": "fixed",
                    "top": "0",
                    "left": "0",
                    "width": "100%",
                    "height": "100%",
                    "zIndex": "999",  # Debajo del texto pero encima de otros elementos
                    "backgroundColor": "rgba(0,0,0,0.01)",  # Transparente pero clickeable
                    "@media (min-width: 769px)": {"display": "none"}
                },
                on_click=TimelineState.toggle_text(item_id)
            )
        ),
        # Mostrar texto en móvil (ajustar z-index)
        rx.cond(
            is_visible,
            rx.box(
                rx.text(
                    button_text,
                    style={
                        "color": "white",
                        "fontSize": "1rem",
                        "backgroundColor": "#3182CE",
                        "padding": "1rem",
                        "borderRadius": "8px",
                        "boxShadow": "0 4px 6px rgba(0,0,0,0.2)",
                        "position": "absolute",
                        "left": "50%",
                        "transform": "translateX(-50%)",
                        "marginTop": "2em",
                        "zIndex": "1000",  # Encima del overlay
                        "width": "max-content",
                        "maxWidth": "80%",
                        # Solo mostrar en móvil
                        "@media (min-width: 769px)": {
                            "display": "none"
                        }
                    }
                )
            ),
        ),
        position="relative",
        margin_y="4em",
        width="100%",
    )

@rx.page(route=navigation.routes.ABOUT_ROUTE)
def about() -> rx.Component:
    language = LanguageState.language
    
    timeline_items = [
        {
            "text": rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][0],
                        translations["en"]["about"]["timeline"][0],
                    ),
            "icon": "graduation_cap",
            "align": "left",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][0],
                        translations["en"]["about"]["time_step"][0],
                    ),            
            "id": "1"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][1],
                        translations["en"]["about"]["timeline"][1],
                    ),
            "icon": "laptop",
            "align": "right",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][1],
                        translations["en"]["about"]["time_step"][1],
                    ),            
            "id": "2"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][2],
                        translations["en"]["about"]["timeline"][2],
                    ),
            "icon": "rocket",
            "align": "left",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][2],
                        translations["en"]["about"]["time_step"][2],
                    ),            
            "id": "3"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][3],
                        translations["en"]["about"]["timeline"][3],
                    ),
            "icon": "biceps-flexed",
            "align": "right",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][3],
                        translations["en"]["about"]["time_step"][3],
                    ),            
            "id": "4"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][4],
                        translations["en"]["about"]["timeline"][4],
                    ),
            "icon": "split",
            "align": "left",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][4],
                        translations["en"]["about"]["time_step"][4],
                    ),            
            "id": "5"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][5],
                        translations["en"]["about"]["timeline"][5],
                    ),
            "icon": "radio",
            "align": "right",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][5],
                        translations["en"]["about"]["time_step"][5],
                    ),            
            "id": "6"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][6],
                        translations["en"]["about"]["timeline"][6],
                    ),
            "icon": "droplets",
            "align": "left",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][6],
                        translations["en"]["about"]["time_step"][6],
                    ),            
            "id": "7"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][7],
                        translations["en"]["about"]["timeline"][7],
                    ),
            "icon": "book-open-text",
            "align": "right",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][7],
                        translations["en"]["about"]["time_step"][7],
                    ),            
            "id": "8"
        },
        {
            "text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["timeline"][8],
                        translations["en"]["about"]["timeline"][8],
                    ),
            "icon": "brain-circuit",
            "align": "left",
            "button_text":  rx.cond(
                        language == "es",
                        translations["es"]["about"]["time_step"][8],
                        translations["en"]["about"]["time_step"][8],
                    ),            
            "id": "9"
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
                        rx.button(  rx.cond(
                        language == "es",
                        translations["es"]["about"]["projects_button"][0],
                        translations["en"]["about"]["projects_button"][0],
                    ),  
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
                "width": "100%",  # Asegurar área clickeable
                "height": "100%",  # Expandir altura completa
            },
        ),
        style={
            "minHeight": "100vh",
            "width": "100%",
            "position": "relative",
        }
    )
