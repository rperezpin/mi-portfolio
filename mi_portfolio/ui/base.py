import reflex as rx
from .navbar import navbar

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.color_mode_cond(
            # En modo claro, aplicamos un fondo con imagen.
            light=rx.box(
                child,
                style={
                    "backgroundImage": "url('/bg3.jpeg')",
                    "backgroundSize": "cover",
                    "backgroundPosition": "center",
                    "backgroundAttachment": "fixed",  # El fondo se queda fijo al hacer scroll
                    "width": "100vw",  # Ocupa el 100% del ancho del viewport
                    "minHeight": "100vh",
                    },
            ),
            # En modo oscuro, solo mostramos el contenido sin imagen de fondo.
            dark=rx.box(
                child,
                style={
                    "backgroundImage": "url('/bg7.jpeg')",
                    "backgroundSize": "cover",
                    "backgroundPosition": "center",
                    "backgroundAttachment": "fixed",  # El fondo se queda fijo al hacer scroll
                    "width": "100vw",  # Ocupa el 100% del ancho del viewport
                    "minHeight": "100vh",
                    },
            ),
        ),
        rx.desktop_only(
            rx.color_mode.button(position="bottom-left")
        ),
    )
