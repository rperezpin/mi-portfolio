import reflex as rx
from .navbar import navbar


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        rx.box(id="top"),  # Punto de referencia para el scroll
        navbar(),        
        rx.color_mode_cond(
            # En modo claro, aplicamos un fondo con imagen.
            light=rx.box(
                child,
                style={
                    "backgroundImage": "url('/bg2.jpg')",
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
                    "backgroundImage": "url('/bg4.jpg')",
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
        # Botón flotante para volver arriba
        rx.box(
            rx.button(
                rx.icon(tag="arrow-up"),
                on_click=rx.scroll_to("top"),
                variant="soft",
                size="3",
                radius="full",
            ),
            position="fixed",
            bottom="2em",
            right="2em",
            z_index="1000",
            style={"opacity": "0.9", ":hover": {"opacity": "1"}}
        )
    )
