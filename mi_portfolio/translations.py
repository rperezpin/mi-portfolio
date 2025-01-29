# state.py
import reflex as rx


class LanguageState(rx.State):
    language: str = "en"  # Default language

    def change_language(self):
        """Switch the language between English and Spanish."""
        self.language = "es" if self.language == "en" else "en"  # Cambio simple de idioma

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
            "title": ["Bienvenido a mi rincón!"],
            "subtitle": ["De alguna forma, este es el proyecto sobre mis proyectos"],
            "home_button": ["Ven a conocer un poco más de mi"],
        },
        "about": {
            "timeline": [
                "Académicamente soy Ingeniero Agrícola y Energético.",
                "Me especialicé con un Máster de Digitalización Agrícola.",
                "Trabajé en proyectos freelance en 2022",
                "Mejorando mis habilidades como full-stack",
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
                "Academically, I am an Agricultural and Energy Engineer.",
                "I specialized with a Master's in Agricultural Digitalization.",
                "Worked on freelance projects in 2022",
                "Improving my skills as a full-stack developer",
            ],
            "projects_button": ["Let's see some of my projects"],
        },
    },
}

