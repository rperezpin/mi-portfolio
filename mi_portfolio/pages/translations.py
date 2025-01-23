# state.py
import reflex as rx

translations = {
    "es": {
        "navbar": {
            "button": ["Switch to English"],
        },
        "about": {
            "title": "Sobre mí",
            "timeline": [
                "Académicamente soy Ingeniero Agrícola y Energético.",
                "Me especialicé con un Máster de Digitalización Agrícola.",
                "Trabajé en proyectos freelance en 2022",
                "Mejorando mis habilidades como full-stack",
            ],
            "button": "Cambiar idioma",
            "projects_button": "Veamos algunos de mis proyectos",
        },
    },
    "en": {
        "navbar": {
            "button": ["Cambiar a Castellano"],
        },
        "about": {
            "title": "About Me",
            "timeline": [
                "Academically, I am an Agricultural and Energy Engineer.",
                "I specialized with a Master's in Agricultural Digitalization.",
                "Worked on freelance projects in 2022",
                "Improving my skills as a full-stack developer",
            ],
            "button": "Change Language",
            "projects_button": "Let's see some of my projects",
        },
    },
}

class LanguageState(rx.State):
    language: str = "en"  # Default language

    def change_language(self):
        """Switch the language between English and Spanish."""
        self.language = "en" if self.language == "es" else "es"
