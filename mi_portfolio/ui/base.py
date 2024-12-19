import reflex as rx

from .navbar import navbar

def base_page(child: rx.Component, *args, **kwargs)-> rx.Component:
    
    return rx.fragment(
        navbar(),
        rx.box(child),
        #rx.logo(),
        rx.desktop_only(
            rx.color_mode.button(position="bottom-left")
            ),
    )
