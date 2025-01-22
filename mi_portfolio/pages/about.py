import reflex as rx
from ..ui.base import base_page
from .. import navigation

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
                "paddingRight": "4rem" if is_left else "0",
                "paddingLeft": "4rem" if not is_left else "0",
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
                    },
                ),
            ),
            rx.hover_card.content(
                rx.box(
                    rx.text(
                        button_text,
                        style={"color": "white", "fontSize": "1rem"},
                    ),
                    style={
                        "backgroundColor": "#3182CE",
                        "padding": "1rem",
                        "borderRadius": "8px",
                        "boxShadow": "0 4px 6px rgba(0,0,0,0.2)",
                        "position": "fixed",
                        "top": "50%",
                        "left": "50%",
                        "transform": "translate(130%)" if is_left else "translate(30%)",
                    },
                ),
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
            "text": "Comencé a estudiar programación en 2020",
            "icon": "graduation_cap",
            "align": "left",
            "button_text": "Aquí aprendí poco",
            "id": "1"
        },
        {
            "text": "Desarrollé mi primera aplicación en 2021",
            "icon": "laptop",
            "align": "right",
            "button_text": "Aquí un poco más",
            "id": "2"
        },
        {
            "text": "Trabajé en proyectos freelance en 2022",
            "icon": "rocket",
            "align": "left",
            "button_text": "Aquí casi na",
            "id": "3"
        },
        {
            "text": "Mejorando mis habilidades como full-stack",
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
                position="relative",
                width="100%",
                max_width="800px",
                margin="auto",
                spacing="4",
            ),
            style={
                "minHeight": "100vh",
                "marginTop": "8rem",
            },
        ),
    )