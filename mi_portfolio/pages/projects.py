import reflex as rx
from ..ui.base import base_page
from .. import navigation
from ..translations import translations, LanguageState

card_style = {
    "padding": "10px",
    "width": "85%",
    "maxHeight": "200px",  # Altura máxima fija
    "height": "auto",  # Mantiene proporción
    "margin": "auto",
    "marginTop": "10px",
    "marginBottom": "10px",
    "borderRadius": "10%",  # Corregido a camelCase
}

# Añadir esta estructura de datos antes de la clase ProjectState
PROJECTS_DATA = [
    {
        "id": "card_0",
        "title": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][0]["title"],
            translations["en"]["projects"]["cards"][0]["title"]
        ),
        "image": "/logo_negro.png",
        "description": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][0]["description"],
            translations["en"]["projects"]["cards"][0]["description"]
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                translations["es"]["projects"]["cards"][0]["details"][i],
                translations["en"]["projects"]["cards"][0]["details"][i]
            ) for i in range(3)
        ],
        "github_url": "https://github.com/rperezpin/mi-portfolio"
    },
    {
        "id": "card_1",
        "title": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][1]["title"],
            translations["en"]["projects"]["cards"][1]["title"]
        ),
        "image": "/books-2247434.svg",
        "description": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][1]["description"],
            translations["en"]["projects"]["cards"][1]["description"]
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                translations["es"]["projects"]["cards"][1]["details"][i],
                translations["en"]["projects"]["cards"][1]["details"][i]
            ) for i in range(6)
        ],
        "github_url": "https://github.com/rperezpin/expressBookReviews"
    },
    {
        "id": "card_2",
        "title": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][2]["title"],
            translations["en"]["projects"]["cards"][2]["title"]
        ),
        "image": "/react-2.svg",
        "description": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][2]["description"],
            translations["en"]["projects"]["cards"][2]["description"]
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                translations["es"]["projects"]["cards"][2]["details"][i],
                translations["en"]["projects"]["cards"][2]["details"][i]
            ) for i in range(5)
        ],
        "github_url": "https://github.com/rperezpin/e-plantShopping"
    },
    {
        "id": "card_3",
        "title": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][3]["title"],
            translations["en"]["projects"]["cards"][3]["title"]
        ),
        "image": "/MQTT 2(1).png",
        "description": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][3]["description"],
            translations["en"]["projects"]["cards"][3]["description"]
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                translations["es"]["projects"]["cards"][3]["details"][i],
                translations["en"]["projects"]["cards"][3]["details"][i]
            ) for i in range(6)
        ],
    },
    {
        "id": "card_4",
        "title": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][4]["title"],
            translations["en"]["projects"]["cards"][4]["title"]
        ),
        "image": "/laravel-2.svg",
        "description": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][4]["description"],
            translations["en"]["projects"]["cards"][4]["description"]
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                translations["es"]["projects"]["cards"][4]["details"][i],
                translations["en"]["projects"]["cards"][4]["details"][i]
            ) for i in range(6)
        ],
    },
    {
        "id": "card_5",
        "title": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][5]["title"],
            translations["en"]["projects"]["cards"][5]["title"]
        ),
        "image": "/fastapi-1.svg",
        "description": rx.cond(
            LanguageState.language == "es",
            translations["es"]["projects"]["cards"][5]["description"],
            translations["en"]["projects"]["cards"][5]["description"]
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                translations["es"]["projects"]["cards"][5]["details"][i],
                translations["en"]["projects"]["cards"][5]["details"][i]
            ) for i in range(6)
        ],
    },
]

# Elimina la importación anterior de State y crea la clase aquí
class ProjectState(rx.State):
    """Estado para proyectos"""
    show_more: dict = {}

    def toggle_show_more(self, card_id: str):
        # Actualizamos el estado creando un nuevo diccionario
        self.show_more = {**self.show_more, card_id: not self.show_more.get(card_id, False)}

def ProjectCard(
    card_id: str,
    title: str,
    image_src: str = "/logo_negro.png",
    description: str = "Descripción del proyecto...",
    details: list = ["- Detalle 1", "- Detalle 2", "- Detalle 3"],
    github_url: str = None  # Nuevo parámetro opcional
):
    return rx.card(
        rx.inset(
            rx.image(
                src=image_src,
                style=card_style,
            ),
            min_height="250px",
            align_content="center",
        ),
        rx.heading(title, size="5"),
        rx.markdown(description),  # Cambiado a markdown para soportar enlaces
        rx.cond(
            ProjectState.show_more[card_id],
            rx.vstack(
                *[rx.text(
                    detail,
                    style={
                        "fontSize": "0.9em",
                        "color": "#4A5568",
                        "marginLeft": "1rem",
                        "marginBottom": "0.5rem",
                        "lineHeight": "1.4"
                    }
                ) for detail in details],
                spacing="2",
                margin_top="1rem",
                style={
                    "opacity": rx.cond(ProjectState.show_more[card_id], 1, 0),
                    "maxHeight": rx.cond(ProjectState.show_more[card_id], "1000px", "0px"),
                    "overflow": "hidden",
                    "transition": "all 1s cubic-bezier(0.4, 0, 0.2, 1)",  # Aumentado a 1 segundo
                    "willChange": "opacity, max-height",
                    "transitionDelay": "0.1s"  # Retardo inicial para sincronizar mejor
                }
            ),
        ),
        rx.button(
            rx.hstack(
                rx.cond(
                    ProjectState.show_more[card_id],
                    rx.cond(
                        LanguageState.language == "es",
                        "Mostrar menos ←",
                        "Hide ←",
                        ),
                    rx.cond(
                        LanguageState.language == "es",
                        "Leer más →",
                        "See more →",
                        ),
                    ),
                rx.cond(
                    github_url,
                    rx.link(
                        rx.icon("github", size=20),
                        href=github_url,
                        margin_left="1em",
                        target="_blank",
                        rel="noopener noreferrer"
                    )
                )
            ),
            on_click=ProjectState.toggle_show_more(card_id),
            variant="soft",
            size="1",
            style={
                "marginTop": "auto",
            }
        ),
        style={
            "boxShadow": "rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px",
            "transition": "transform 0.9s ease-in-out, height 1s ease-in-out",  # Sincronizado con 1s
            "_hover": {"transform": "scale(1.02)"}
        }
    )

@rx.page(route=navigation.routes.PROJECTS_ROUTE)
def projects() -> rx.Component:
    language = LanguageState.language

    return base_page(
        rx.vstack(
            rx.heading(rx.cond(
                        language == "es",
                        translations["es"]["projects"]["title"][0],
                        translations["en"]["projects"]["title"][0],
                    ),
                    size="9", align="center", margin_top="4rem"),
            rx.grid(
                *[ProjectCard(
                    card_id=project["id"],
                    title=project["title"],
                    image_src=project["image"],
                    description=project["description"],
                    details=project["details"],
                    github_url=project.get("github_url")
                ) for project in PROJECTS_DATA],
                gap="2rem",  # Más espacio entre tarjetas
                padding="2rem",  # Padding adicional
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
        )
    )
