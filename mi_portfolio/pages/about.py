import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..translations import translations, LanguageState
import time

class TimelineState(rx.State):
    # Estado para controlar qué textos están visibles
    visible_text: str | None = None
    hovered_text: str | None = None  # New state for hover
    last_hover_time: float = 0.0  # Track last hover time

    def toggle_text(self, text_id: str):
        """Alterna la visibilidad del texto."""
        self.visible_text = None if self.visible_text == text_id else text_id

    def set_hovered_text(self, text_id: str, is_hovered: bool):
        """Set the hovered text state with debounce."""
        current_time = time.time()
        if current_time - self.last_hover_time > 0.1:  # 100ms debounce
            self.hovered_text = text_id if is_hovered else None
            self.last_hover_time = current_time

    def reset_visible_text(self):
        """Reset the visible text."""
        self.visible_text = None

    def handle_global_click(self):
        """Hide visible text when clicking outside."""
        if self.visible_text:
            self.visible_text = None

def timeline_item(text: str, icon: str, align: str, button_text: str, item_id: str) -> rx.Component:
    """Crea un elemento individual de la línea de tiempo."""
    is_left = align == "left"
    is_visible = TimelineState.visible_text == item_id
    is_hovered = TimelineState.hovered_text == item_id  # Check hover state

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
        # Replace hover card with a tooltip for mobile compatibility
        rx.tooltip(
            rx.button(
                "",
                on_click=lambda: TimelineState.toggle_text(item_id),
                on_mouse_enter=lambda: TimelineState.set_hovered_text(item_id, True),
                on_mouse_leave=lambda: TimelineState.set_hovered_text(item_id, False),
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
                },
            ),
            label=button_text,
            background_color="#3182CE",
            color="white",
            border_radius="8px",
            padding="1rem",
            placement="top" if is_left else "bottom",
        ),
        # Add conditional box for click or hover state using bitwise operators
        rx.cond(
            is_visible | is_hovered,
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
                        "zIndex": "1000",
                        "width": "max-content",
                        "maxWidth": "80%",
                    }
                )
            ),
            rx.box()
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
            },
        ),
            on_click=TimelineState.handle_global_click,
    )
