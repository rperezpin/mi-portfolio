# state.py
import reflex as rx


class LanguageState(rx.State):
    language: str = "en"  # Default language

    def change_language(self):
        """Switch the language between English and Spanish."""
        self.language = "en" if self.language == "es" else "es"  # Cambio simple de idioma

translations = {
    "es": {
        "navbar": {
            "button": ["Switch to English"],
            "headers": [
                "Inicio",
                "Sobre mi",
                "Proyectos",
                "Contacto",
                ],
        },
        "home": {
            "title": ["¡Bienvenido a mi rincón!"],
            "subtitle": ["De alguna forma, este es el proyecto sobre mis proyectos"],
            "home_button": ["Ven a conocer un poco más de mi"],
        },
        "about": {
            "timeline": [
                "Soy Ingeniero Agrícola y Energético con especialización en Digitalización Agrícola.",
                "Descubrí mi pasión por el análisis de datos aplicado a la agricultura inteligente.",
                "Inicié mi carrera como Data Analyst, donde puse en práctica mis conocimientos técnicos.",
                "Gané experiencia trabajando con Big Data y técnicas de Machine Learning en el sector agro.",
                "Buscando nuevos retos, evolucioné profesionalmente hacia proyectos diferentes.",
                "Comencé a desarrollar soluciones basadas en IoT para la agricultura de precisión.",
                "Participé en el desarrollo integral de una plataforma tecnológica para la optimización agrícola.",
                "Nunca he dejado de formarme en tecnologías emergentes y metodologías ágiles.",
                "Hoy sigo aprendiendo y aplicando conocimientos en digitalización y desarrollo."
            ],
            "time_step": [
                "Mi formación me abrió las puertas a mis primeros trabajos como ingeniero técnico.",
                "Fue entonces cuando escribí mis primeras líneas de código aplicadas al sector.",
                "Aprendí a analizar y modelar datos para la predicción de cosechas y optimización de cultivos.",
                "Me especialicé en herramientas clave como Python, R, SQL y visualización de datos.",
                "Perfeccioné mis habilidades en análisis avanzado de datos, IA y aprendizaje automático.",
                "Aunque seguí en el ámbito de la digitalización agrícola, la exploré desde otra perspectiva.",
                "Desarrollé software para plataformas de monitorización agrícola e IoT.",
                "Trabajé en la configuración de servidores, broker MQTT, bases de datos y apps de visualización.",
                "Profundicé en Ingeniería de Datos, Desarrollo de Aplicaciones, Inteligencia Artificial...",
                "Y objetivo es seguir creciendo y abrirme a todo tipo de sectores."
            ],
            "projects_button": ["Veamos algunos de mis proyectos"],
        },
        "projects": {
            "title":["Estos son algunos de mis proyectos"],
            "cards": [
                {
                    "id": "card_0",
                    "title": "Portfolio Reflex",
                    "description": "Mi propio portfolio desarrollado con Reflex",
                    "details": [
                        "Tecnologías: Python, Reflex",
                        "Características: Responsive design",
                        "Deploy: Reflex Cloud"
                    ]
                },
                {
                    "id": "card_1",
                    "title": "API de Librería con Autenticación",
                    "description": "Sistema backend para gestión de libros y reseñas. Ofrece:",
                    "details": [
                        "📚 Búsqueda de libros por ISBN, autor o título",
                        "🔐 Autenticación JWT con registro/login de usuarios",
                        "✏️ Sistema de reseñas personalizadas (CRUD)",
                        "🚀 Desarrollado con Node.js/Express y almacenamiento en memoria",
                        "🛠️ Tecnologías principales: Express.js, JWT, REST API",
                        "Ideal para aprender sobre autenticación segura y manejo de sesiones en APIs"
                    ]
                },
                {
                    "id": "card_2",
                    "title": "API REST con FastAPI",
                    "description": "Backend moderno para sistema de gestión de contenidos. Incluye:",
                    "details": [
                        "🚀 Creación de endpoints REST con autenticación JWT",
                        "📄 Documentación interactiva automática con Swagger UI",
                        "🔐 Sistema de roles y permisos granular",
                        "🐳 Dockerización para despliegue en contenedores",
                        "🛠️ Tecnologías principales: FastAPI, PostgreSQL, Docker, JWT",
                        "🧩 Optimizado para alta concurrencia con async/await"
                    ]
                }
            ],
            "timeline": [
                "Soy Ingeniero Agrícola y Energético con especialización en Digitalización Agrícola.",
                "Descubrí mi pasión por el análisis de datos aplicado a la agricultura inteligente.",
                "Inicié mi carrera como Data Analyst, donde puse en práctica mis conocimientos técnicos.",
                "Gané experiencia trabajando con Big Data y técnicas de Machine Learning en el sector agro.",
                "Buscando nuevos retos, evolucioné profesionalmente hacia proyectos diferentes.",
                "Comencé a desarrollar soluciones basadas en IoT para la agricultura de precisión.",
                "Participé en el desarrollo integral de una plataforma tecnológica para la optimización agrícola.",
                "Nunca he dejado de formarme en tecnologías emergentes y metodologías ágiles.",
                "Hoy sigo aprendiendo y aplicando conocimientos en digitalización y desarrollo."
            ],
            "time_step": [
                "Mi formación me abrió las puertas a mis primeros trabajos como ingeniero técnico.",
                "Fue entonces cuando escribí mis primeras líneas de código aplicadas al sector.",
                "Aprendí a analizar y modelar datos para la predicción de cosechas y optimización de cultivos.",
                "Me especialicé en herramientas clave como Python, R, SQL y visualización de datos.",
                "Perfeccioné mis habilidades en análisis avanzado de datos, IA y aprendizaje automático.",
                "Aunque seguí en el ámbito de la digitalización agrícola, la exploré desde otra perspectiva.",
                "Desarrollé software para plataformas de monitorización agrícola e IoT.",
                "Trabajé en la configuración de servidores, broker MQTT, bases de datos y apps de visualización.",
                "Profundicé en Ingeniería de Datos, Desarrollo de Aplicaciones, Inteligencia Artificial...",
                "Y objetivo es seguir creciendo y abrirme a todo tipo de sectores."
            ],
            "projects_button": ["Veamos algunos de mis proyectos"],
        },
    },
    "en": {
        "navbar": {
            "button": ["Cambiar a Castellano"],
            "headers": [
                "Home",
                "About Me",
                "Projects",
                "Contact",
                ],
        },
        "home": {
            "title": ["Welcome to my place!"],
            "subtitle": ["In some way, this is the project about all my projects"],
            "home_button": ["Come to know a little more about me"],
        },
        "about": {
            "timeline": [
                "I am an Agricultural and Energy Engineer with a specialization in Agricultural Digitalization.",
                "I discovered my passion for data analysis applied to smart farming.",
                "I started my career as a Data Analyst, where I put my technical knowledge into practice.",
                "I gained experience working with Big Data and Machine Learning techniques in the agricultural sector.",
                "Seeking new challenges, I evolved professionally into different projects.",
                "I began developing IoT-based solutions for precision agriculture.",
                "I participated in the end-to-end development of a technology platform for agricultural optimization.",
                "I have never stopped learning about emerging technologies and agile methodologies.",
                "Today, I continue to learn and apply knowledge in digitalization and development."
            ],
            "time_step": [
                "My education opened the doors to my first jobs as a technical engineer.",
                "That's when I wrote my first lines of code applied to the sector.",
                "I learned to analyze and model data for crop prediction and optimization.",
                "I specialized in key tools such as Python, R, SQL, and data visualization.",
                "I honed my skills in advanced data analysis, AI, and machine learning.",
                "Although I remained in the field of agricultural digitalization, I explored it from a different perspective.",
                "I developed software for agricultural monitoring platforms and IoT solutions.",
                "I worked on server configuration, MQTT brokers, databases, and visualization apps.",
                "I deepened my knowledge in Data Engineering, Application Development, Artificial Intelligence...",
                "My goal is to continue growing and expand into different industries."
            ],
            "projects_button": ["Let's see some of my projects"],
        },
        "projects": {
            "title": ["These are some of my projects"],
            "cards": [
                {
                    "id": "card_0",
                    "title": "Reflex Portfolio",
                    "description": "My own portfolio developed with Reflex",
                    "details": [
                        "Technologies: Python, Reflex",
                        "Features: Responsive design", 
                        "Deployment: Reflex Cloud"
                    ]
                },
                {
                    "id": "card_1", 
                    "title": "Bookstore API with Authentication",
                    "description": "Backend system for book and review management. Features:",
                    "details": [
                        "📚 Book search by ISBN, author or title",
                        "🔐 JWT authentication with user registration/login",
                        "✏️ Custom review system (CRUD operations)",
                        "🚀 Built with Node.js/Express and in-memory storage",
                        "🛠️ Main technologies: Express.js, JWT, REST API",
                        "Ideal for learning secure authentication and session management in APIs"
                    ]
                },
                {
                    "id": "card_2",
                    "title": "REST API with FastAPI",
                    "description": "Modern backend for content management system. Includes:",
                    "details": [
                        "🚀 REST endpoints creation with JWT authentication",
                        "📄 Automatic interactive documentation with Swagger UI",
                        "🔐 Granular role-based permission system",
                        "🐳 Dockerized for container deployment",
                        "🛠️ Main technologies: FastAPI, PostgreSQL, Docker, JWT",
                        "🧩 Optimized for high concurrency with async/await"
                    ]
                }
            ],
            "timeline": [
                "Soy Ingeniero Agrícola y Energético con especialización en Digitalización Agrícola.",
                "Descubrí mi pasión por el análisis de datos aplicado a la agricultura inteligente.",
                "Inicié mi carrera como Data Analyst, donde puse en práctica mis conocimientos técnicos.",
                "Gané experiencia trabajando con Big Data y técnicas de Machine Learning en el sector agro.",
                "Buscando nuevos retos, evolucioné profesionalmente hacia proyectos diferentes.",
                "Comencé a desarrollar soluciones basadas en IoT para la agricultura de precisión.",
                "Participé en el desarrollo integral de una plataforma tecnológica para la optimización agrícola.",
                "Nunca he dejado de formarme en tecnologías emergentes y metodologías ágiles.",
                "Hoy sigo aprendiendo y aplicando conocimientos en digitalización y desarrollo."
            ],
            "time_step": [
                "Mi formación me abrió las puertas a mis primeros trabajos como ingeniero técnico.",
                "Fue entonces cuando escribí mis primeras líneas de código aplicadas al sector.",
                "Aprendí a analizar y modelar datos para la predicción de cosechas y optimización de cultivos.",
                "Me especialicé en herramientas clave como Python, R, SQL y visualización de datos.",
                "Perfeccioné mis habilidades en análisis avanzado de datos, IA y aprendizaje automático.",
                "Aunque seguí en el ámbito de la digitalización agrícola, la exploré desde otra perspectiva.",
                "Desarrollé software para plataformas de monitorización agrícola e IoT.",
                "Trabajé en la configuración de servidores, broker MQTT, bases de datos y apps de visualización.",
                "Profundicé en Ingeniería de Datos, Desarrollo de Aplicaciones, Inteligencia Artificial...",
                "Y objetivo es seguir creciendo y abrirme a todo tipo de sectores."
            ],
            "projects_button": ["Veamos algunos de mis proyectos"],
        },
    },
}

