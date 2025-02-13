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
        "title": "Portfolio Reflex",
        "image": "/logo_negro.png",
        "description": "Mi propio portfolio desarrollado con Reflex",
        "details": [
            "Tecnologías: Python, Reflex",
            "Características: Responsive design",
            "Deploy: Reflex Cloud"
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
                    "🛠️ Tecnologías principales: Express.js, JWT, REST API",
                    "Ideal para aprender sobre autenticación segura y manejo de sesiones en APIs",
                    ],
        "github_url": "https://github.com/rperezpin/expressBookReviews"
    },
    {
        "id": "card_2",
        "title": "E-Plant Shopping con React",
        "image": "/react-2.svg",
        "description": "Plataforma e-commerce especializada en venta de plantas con funcionalidades específicas. Ofrece:",
        "details": ["🛒 Sistema de carrito interactivo con gestión de cantidades",
                    "📦 Persistencia de estado del carrito usando Redux Toolkit",
                    "🖼️ Catálogo visual con cards de productos detalladas",
                    "🔄 Actualización en tiempo real del contador del carrito",
                    "🛠️ Tecnologías principales: React + Vite, Redux Toolkit",
                    "Práctica para la implementación de una plataforma e-commerce con carrito interactivo.",
                    ],
        "github_url": "https://github.com/rperezpin/e-plantShopping"
    },
    {
        "id": "card_3",
        "title": "Broker MQTT para IoT con Node.js",
        "image": "/MQTT 2(1).png",
        "description": "Sistema de intermediario IoT para procesamiento de datos en tiempo real. Funcionalidades clave:",
        "details": [
            "📡 Implementación de broker MQTT escalable",
            "🔁 Transformación de datos con pipelines personalizados",
            "🗃️ Almacenamiento en MySQL con modelos de datos optimizados",
            "🔒 Seguridad: Autenticación JWT + TLS para comunicaciones",
            "🛠️ Tecnologías principales: Node.js, MySQL",
            "🧩 Arquitectura modular para fácil expansión"
        ],
    },
    {
        "id": "card_4",
        "title": "Monitorización IoT con Laravel",
        "image": "/laravel-2.svg",
        "description": "Sistema completo para gestión y visualización de datos IoT. Características principales:",
        "details": [
            "🌡️ Recepción de datos en tiempo real desde sensores IoT",
            "📊 Dashboard interactivo con gráficos usando HighCharts",
            "📈 Almacenamiento histórico en base de datos MySQL",
            "🔔 Sistema de alertas configurable por umbrales",
            "🛠️ Tecnologías principales: Laravel, MySQL, Bootstrap",
            "🧩 Arquitectura escalable para manejar múltiples dispositivos simultáneamente"
        ],
    },
    {
        "id": "card_5",
        "title": "API REST con FastAPI",
        "image": "/fastapi-1.svg",
        "description": "Backend moderno para sistema de gestión de contenidos. Incluye:",
        "details": [
            "🚀 Creación de endpoints REST con autenticación JWT",
            "📄 Documentación interactiva automática con Swagger UI",
            "🔐 Sistema de roles y permisos granular",
            "🐳 Dockerización para despliegue en contenedores",
            "🛠️ Tecnologías principales: FastAPI, PostgreSQL, Docker, JWT",
            "🧩 Optimizado para alta concurrencia con async/await"
        ],
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
                "alignSelf": "flex-end"
            }
        ),
        style={  # Mejoras de estilo
            "boxShadow": "rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px",
            "transition": "transform 0.2s",
            "_hover": {"transform": "scale(1.02)"}
        }
    )

@rx.page(route=navigation.routes.PROJECTS_ROUTE)
def projects() -> rx.Component:
    language = LanguageState.language

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
