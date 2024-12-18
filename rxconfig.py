import reflex as rx

config = rx.Config(
    app_name="mi_portfolio",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)