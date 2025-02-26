import reflex as rx
import asyncio
from ..ui.base import base_page
from .. import navigation
from ..translations import translations, LanguageState

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    @rx.var
    def thank_you(self) -> str:  # Added type annotation here
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"

    async def handle_submit(self, forma_data: dict):
        print(forma_data)
        self.form_data = forma_data
        self.did_submit = True
        yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact() -> rx.Component:
    language = LanguageState.language
    my_form = rx.form(
            rx.vstack(
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                ),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),
                rx.input(
                    placeholder="Email",
                    name="last_name",
                    type="email"
                ),
                rx.text_area(
                    placeholder="Your text here",
                    name="message",
                    type="text"
                ),
                rx.button(
                 rx.cond(
                        language == "es",
                        translations["es"]["contact"]["button"][0],
                        translations["en"]["contact"]["button"][0],
                    ),
                    type="submit"),

            align="center"
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        )
    my_child = rx.vstack(
            rx.heading(
                 rx.cond(
                        language == "es",
                        translations["es"]["contact"]["title"][0],
                        translations["en"]["contact"]["title"][0],
                    ),
                    size="9"),
            rx.text(
                 rx.cond(
                        language == "es",
                        translations["es"]["contact"]["subtitle"][0],
                        translations["en"]["contact"]["subtitle"][0],
                    ),
                size="5",
            ),
            rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
            my_form,
            rx.hstack(
                rx.link(
                    rx.icon("github"),
                    href="https://github.com/rperezpin",
                    target="_blank",
                    rel="noopener noreferrer",
                    color_scheme="gray"
                ),
                rx.link(
                    rx.icon("linkedin"),
                    href="https://www.linkedin.com/in/rub%C3%A9n-p%C3%A9rez-izuel-a02607189/",
                    target="_blank",
                    rel="noopener noreferrer",
                    color_scheme="blue"
                ),
                spacing="4",
                align="center"
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
        )
    return base_page(my_child)