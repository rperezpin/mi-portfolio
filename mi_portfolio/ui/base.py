import reflex as rx
from .navbar import navbar


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        rx.box(id="top"),  # Punto de referencia para el scroll
        rx.box(
            navbar(),
            position="fixed",
            top="0",
            left="0",
            right="0",
            z_index="1000",
            style={
                "backdropFilter": "blur(10px)",
                "backgroundColor": rx.color_mode_cond(
                    light="rgba(255, 255, 255, 0.7)",  # Blanco semitransparente
                    dark="rgba(0, 0, 0, 0.5)"  # Negro semitransparente
                ),
            }
        ),
        rx.color_mode_cond(
            # En modo claro, aplicamos un fondo con imagen.
            light=rx.box(
                child,
                style={
                    "backgroundImage": "url('/bg2.jpg')",
                    "backgroundSize": "cover",
                    "paddingTop": "80px",  # Espacio para la navbar fija
                    "backgroundPosition": "center",
                    "backgroundAttachment": "fixed",  # El fondo se queda fijo al hacer scroll
                    "width": "100vw",  # Ocupa el 100% del ancho del viewport
                    "height": "100%",  # Nueva propiedad
                    "minHeight": "-webkit-fill-available; min-height: 100vh",  # Fix para Safari
                    "position": "relative",  # Mejor manejo de posición
                },
            ),
            # En modo oscuro, solo mostramos el contenido sin imagen de fondo.
            dark=rx.box(
                child,
                style={
                    "backgroundImage": "url('/bg4.jpg')",
                    "backgroundSize": "cover",
                    "paddingTop": "80px",  # Espacio para la navbar fija
                    "backgroundPosition": "center",
                    "backgroundAttachment": "fixed",  # El fondo se queda fijo al hacer scroll
                    "width": "100vw",  # Ocupa el 100% del ancho del viewport
                    "height": "100%",  # Nueva propiedad
                    "minHeight": "-webkit-fill-available; min-height: 100vh",  # Fix para Safari
                    "position": "relative",  # Mejor manejo de posición
                },
            ),
        ),
        rx.tablet_and_desktop(
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
