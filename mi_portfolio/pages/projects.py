import reflex as rx
from ..ui.base import base_page
from .. import navigation

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
        "title": "Portfolio Reflex",
        "image": "/logo_negro.png",
        "description": "Mi propio portfolio desarrollado con Reflex",
        "details": [
            "Tecnologías: Python, Reflex",
            "Características: Responsive design",
            "Deploy: Docker y AWS"
        ],
        "github_url": "https://github.com/rperezpin/mi-portfolio"
    },
    {
        "id": "card_1",
        "title": "API de Librería con Autenticación",
        "image": "/books-2247434.svg",
        "description": "Sistema backend para gestión de libros y reseñas. Ofrece:",
        "details": ["📚 Búsqueda de libros por ISBN, autor o título",
                    "🔐 Autenticación JWT con registro/login de usuarios",
                    "✏️ Sistema de reseñas personalizadas (CRUD)",
                    "🚀 Desarrollado con Node.js/Express y almacenamiento en memoria",
                    "Tecnologías principales: Express.js, JWT, REST API",
                    "Ideal para aprender sobre autenticación segura y manejo de sesiones en APIs",
                    ],
        "github_url": "https://github.com/rperezpin/expressBookReviews"
    },
    {
        "id": "card_2",
        "title": "E-Plant Shopping con React",
        "image": "/Captura desde 2025-02-11 20-35-48.png",
        "description": "Plataforma e-commerce especializada en venta de plantas con funcionalidades específicas. Ofrece:",
        "details": ["🛒 Sistema de carrito interactivo con gestión de cantidades",
                    "📦 Persistencia de estado del carrito usando Redux Toolkit",
                    "🖼️ Catálogo visual con cards de productos detalladas",
                    "🔄 Actualización en tiempo real del contador del carrito",
                    "⚛️ Arquitectura React con componentes modulares",
                    "🧮 Cálculos automáticos de totales (por ítem y general)",
                    "Tecnologías principales: React + Vite, Redux Toolkit",
                    "Práctica para la implementación de una plataforma e-commerce con carrito interactivo.",
                    ],
        "github_url": "https://github.com/rperezpin/e-plantShopping"
    },
    # Añadir los otros 4 proyectos aquí con sus datos específicos
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
            side="top",
            pb="current",
        ),
        rx.heading(title, size="5"),
        rx.markdown(description),  # Cambiado a markdown para soportar enlaces
        rx.cond(
            ProjectState.show_more[card_id],
            rx.vstack(
                *[rx.text(
                    detail,
                    style={  # Nuevo estilo para los detalles
                        "fontSize": "0.9em",
                        "color": "#4A5568",
                        "marginLeft": "1rem",
                        "marginBottom": "0.5rem",
                        "lineHeight": "1.4"
                    }
                ) for detail in details],
                spacing="2",
                margin_top="1rem"
            ),
        ),
        rx.button(
            rx.hstack(
                rx.cond(
                    ProjectState.show_more[card_id],
                    "Mostrar menos ←",
                    "Leer más →",
                ),
                rx.cond(  # Icono GitHub si hay URL
                    github_url,
                    rx.link(
                        rx.icon("github", size=20),
                        href=github_url,
                        margin_left="1em",
                        target="_blank",  # Nueva pestaña
                        rel="noopener noreferrer"  # Seguridad para nuevas pestañas
                    )
                )
            ),
            on_click=ProjectState.toggle_show_more(card_id),
            variant="soft",
            size="1",
            style={"marginTop": "1em"}
        ),
        style={  # Mejoras de estilo
            "boxShadow": "rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px",
            "transition": "transform 0.2s",
            "_hover": {"transform": "scale(1.02)"}
        }
    )

@rx.page(route=navigation.routes.PROJECTS_ROUTE)
def projects() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Here comes everything I've done", size="9", align="center", margin_top="4rem"),
            rx.text(
                "Look at this",
                size="5",
                align="center",
                margin_bottom="2rem"
            ),
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
