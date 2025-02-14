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
            "Broker MQTT para IoT con Node.js",
            "IoT MQTT Broker with Node.js"
        ),
        "image": "/MQTT 2(1).png",
        "description": rx.cond(
            LanguageState.language == "es",
            "Sistema de intermediario IoT para procesamiento de datos en tiempo real. Funcionalidades clave:",
            "IoT middleware system for real-time data processing. Key features:"
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                [
                    "📡 Implementación de broker MQTT escalable",
                    "🔁 Transformación de datos con pipelines personalizados",
                    "🗃️ Almacenamiento en MySQL con modelos de datos optimizados",
                    "🔒 Seguridad: Autenticación JWT + TLS para comunicaciones",
                    "🛠️ Tecnologías principales: Node.js, MySQL",
                    "🧩 Arquitectura modular para fácil expansión"
                ][i],
                [
                    "📡 Scalable MQTT broker implementation",
                    "🔁 Data transformation with custom pipelines",
                    "🗃️ MySQL storage with optimized data models",
                    "🔒 Security: JWT authentication + TLS communications",
                    "🛠️ Main technologies: Node.js, MySQL",
                    "🧩 Modular architecture for easy expansion"
                ][i]
            ) for i in range(6)
        ],
    },
    {
        "id": "card_4",
        "title": rx.cond(
            LanguageState.language == "es",
            "Monitorización IoT con Laravel",
            "IoT Monitoring with Laravel"
        ),
        "image": "/laravel-2.svg",
        "description": rx.cond(
            LanguageState.language == "es",
            "Sistema completo para gestión y visualización de datos IoT. Características principales:",
            "Complete system for IoT data management and visualization. Key features:"
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                [
                    "🌡️ Recepción de datos en tiempo real desde sensores IoT",
                    "📊 Dashboard interactivo con gráficos usando HighCharts",
                    "📈 Almacenamiento histórico en base de datos MySQL",
                    "🔔 Sistema de alertas configurable por umbrales",
                    "🛠️ Tecnologías principales: Laravel, MySQL, Bootstrap",
                    "🧩 Arquitectura escalable para manejar múltiples dispositivos simultáneamente"
                ][i],
                [
                    "🌡️ Real-time data reception from IoT sensors",
                    "📊 Interactive dashboard with HighCharts",
                    "📈 Historical storage in MySQL database",
                    "🔔 Configurable alert system by thresholds",
                    "🛠️ Main technologies: Laravel, MySQL, Bootstrap",
                    "🧩 Scalable architecture for handling multiple devices simultaneously"
                ][i]
            ) for i in range(6)
        ],
    },
    {
        "id": "card_5",
        "title": rx.cond(
            LanguageState.language == "es",
            "API REST con FastAPI",
            "REST API with FastAPI"
        ),
        "image": "/fastapi-1.svg",
        "description": rx.cond(
            LanguageState.language == "es",
            "Backend moderno para sistema de gestión de contenidos. Incluye:",
            "Modern backend for content management system. Includes:"
        ),
        "details": [
            rx.cond(
                LanguageState.language == "es",
                [
                    "🚀 Creación de endpoints REST con autenticación JWT",
                    "📄 Documentación interactiva automática con Swagger UI",
                    "🔐 Sistema de roles y permisos granular",
                    "🐳 Dockerización para despliegue en contenedores",
                    "🛠️ Tecnologías principales: FastAPI, PostgreSQL, Docker, JWT",
                    "🧩 Optimizado para alta concurrencia con async/await"
                ][i],
                [
                    "🚀 REST API creation with JWT authentication",
                    "📄 Interactive Swagger UI documentation",
                    "🔐 Granular role and permission system",
                    "🐳 Dockerization for deployment in containers",
                    "🛠️ Main technologies: FastAPI, PostgreSQL, Docker, JWT",
                    "�� Optimized for high concurrency with async/await"
                ][i]
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
