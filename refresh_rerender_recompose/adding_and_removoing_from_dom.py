from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Horizontal


class HappyApp(App):
    def compose(self) -> ComposeResult:
        with Static():
            pass
        with Horizontal():
            yield Button("Add", variant="success", id="add-bt")
            yield Button("Remove", variant="error", id="remove-bt")

    @on(Button.Pressed, "#add-bt")
    def add_button(self):
        self.query_one(Static).mount(Button("Placeholder"))

    @on(Button.Pressed, "#remove-bt")
    def remove_button(self):
        children = self.query_one(Static).children
        if children:
            children[-1].remove()


if __name__ == "__main__":
    HappyApp().run()

