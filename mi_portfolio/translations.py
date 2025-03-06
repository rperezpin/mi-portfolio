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
            "title": ["¡Bienvenido/a a mi Portfolio Digital!"],
            "subtitle": ["Este sitio es, en cierto modo, el proyecto que reúne todos mis proyectos."],
            "home_button": ["Descubre más sobre mí"],
        },
        "about": {
            "timeline": [
                "Ingeniero Agrícola y Energético especializado en Transformación Digital Agrícola.",
                "Descubrí mi pasión por el análisis de datos aplicado a la agricultura inteligente.",
                "Comencé mi carrera como Data Analyst, donde puse en práctica mis conocimientos técnicos.",
                "Gané experiencia trabajando con Big Data y técnicas de Machine Learning en el sector agro.",
                "Buscando nuevos retos, evolucioné profesionalmente hacia proyectos diferentes.",
                "Comencé a desarrollar soluciones basadas en IoT para la agricultura de precisión.",
                "Participé en el desarrollo integral de una plataforma tecnológica para la optimización agrícola.",
                "Nunca he dejado de formarme en tecnologías emergentes y metodologías nuevas.",
                "Actualmente, sigo perfeccionando mis conocimientos en digitalización y desarrollo tecnológico."
            ],
            "time_step": [
                "Mi formación me abrió las puertas a mis primeros trabajos como ingeniero técnico.",
                "Fue entonces cuando escribí mis primeras líneas de código aplicadas al sector.",
                "Aprendí a analizar y modelar datos para la predicción de cosechas y optimización de cultivos.",
                "Me especialicé en herramientas clave como Python, R, SQL y análisis de datos.",
                "Aunque seguí en el ámbito de la digitalización agrícola, la exploré desde otra perspectiva.",
                "Desarrollé software para plataformas de monitorización agrícola e IoT.",
                "Trabajé en la configuración de servidores, broker MQTT, bases de datos y apps de visualización.",
                "Profundicé en Ingeniería de Datos, Desarrollo de Aplicaciones, Inteligencia Artificial...",
                "Mi objetivo es seguir creciendo y explorar oportunidades en todo tipo de sectores."
            ],
            "projects_button": ["Explora algunos de mis proyectos"],
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
                },
                {
                    "id": "card_3",
                    "title": "Broker MQTT para IoT con Node.js",
                    "description": "Sistema de intermediario IoT para procesamiento de datos en tiempo real. Funcionalidades clave:",
                    "details": [
                        "📡 Implementación de broker MQTT escalable",
                        "🔁 Transformación de datos con pipelines personalizados",
                        "🗃️ Almacenamiento en MySQL con modelos de datos optimizados",
                        "🔒 Seguridad: Autenticación JWT + TLS para comunicaciones",
                        "🛠️ Tecnologías principales: Node.js, MySQL",
                        "🧩 Arquitectura modular para fácil expansión"
                    ]
                },
                {
                    "id": "card_4",
                    "title": "Monitorización IoT con Laravel",
                    "description": "Sistema completo para gestión y visualización de datos IoT. Características principales:",
                    "details": [
                        "🌡️ Recepción de datos en tiempo real desde sensores IoT",
                        "📊 Dashboard interactivo con gráficos usando HighCharts",
                        "📈 Almacenamiento histórico en base de datos MySQL",
                        "🔔 Sistema de alertas configurable por umbrales",
                        "🛠️ Tecnologías principales: Laravel, MySQL, Bootstrap",
                        "🧩 Arquitectura escalable para manejar múltiples dispositivos simultáneamente"
                    ]
                },
                {
                    "id": "card_5",
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
            "contact_button": ["¿Tienes una idea? ¡Compártela conmigo!"],
        },
        "contact": {
            "title": ["Contáctame"],
            "subtitle": ["¡Estoy disponible para nuevas oportunidades y colaboraciones!"],
            "button": ["Enviar mensaje"],
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
            "title": ["Welcome to my Digital Portfolio"],
            "subtitle": ["In some way, this is the project about all my projects"],
            "home_button": ["Learn more about me"],
        },
        "about": {
            "timeline": [
                "Agricultural and Energy Engineer specializing in Agricultural Digitalization.",
                "I discovered my passion for data analysis applied to smart farming.",
                "I started my career as a Data Analyst, applying my technical expertise.",
                "I gained experience in Big Data and Machine Learning within the agricultural sector.",
                "Seeking new challenges, I evolved professionally into different projects.",
                "I began developing IoT-based solutions for precision agriculture.",
                "I participated in the end-to-end development of a technology platform for agricultural optimization.",
                "I have never stopped learning about emerging technologies and new methodologies.",
                "Currently, I continue to refine my expertise in digitalization and technological development."
            ],
            "time_step": [
                "My education opened the doors to my first jobs as a technical engineer.",
                "That's when I wrote my first lines of code applied to the sector.",
                "I learned to analyze and model data for crop prediction and optimization.",
                "I specialized in key tools such as Python, R, SQL, and data analysis.",
                "Although I remained in the field of agricultural digitalization, I explored it from a different perspective.",
                "I developed software for agricultural monitoring platforms and IoT solutions.",
                "I worked on server configuration, MQTT brokers, databases, and visualization apps.",
                "I deepened my knowledge in Data Engineering, Application Development, Artificial Intelligence...",
                "My goal is to continue growing and expand into different industries."
            ],
            "projects_button": ["Explore some of my projects"],
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
                },
                {
                    "id": "card_3",
                    "title": "Broker MQTT for IoT with Node.js",
                    "description": "IoT intermediary system for real-time data processing. Key functionalities:",
                    "details": [
                        "📡 Scalable MQTT broker implementation",
                        "🔁 Data transformation with customized pipelines",
                        "🗃️ MySQL-based storage with optimized data models",
                        "🔒 Security: JWT authentication + TLS for communications",
                        "🛠️ Main technologies: Node.js, MySQL",
                        "🧩 Modular architecture for easy expansion"
                    ]
                },
                {
                    "id": "card_4",
                    "title": "IoT Monitoring with Laravel",
                    "description": "Complete system for IoT data management and visualization. Main features:",
                    "details": [
                        "🌡️ Real-time data reception from IoT sensors",
                        "📊 Interactive dashboard with HighCharts graphics",
                        "📈 Historical storage in MySQL database",
                        "🔔 Configurable alert system by thresholds",
                        "🛠️ Main technologies: Laravel, MySQL, Bootstrap",
                        "🧩 Scalable architecture for handling multiple devices simultaneously"
                    ]
                },
                {
                    "id": "card_5",
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
            "contact_button": ["Have an idea? Let’s discuss it!"],
        },
        "contact": {
            "title": ["Get in Touch"],
            "subtitle": ["I’m open to new opportunities and collaborations!"],
            "button": ["Submit Message"],
        },
    },
}

