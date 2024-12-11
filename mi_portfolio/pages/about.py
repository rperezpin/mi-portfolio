import reflex as rx

def about() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Something about me", size="9"),
            rx.text(
                "Let's talk something about what I am:",
                size="5",
            ),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        )