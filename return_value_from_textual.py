from textual.app import App, ComposeResult
from textual.widgets import Button


class ExitApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Exit")

    def on_button_pressed(self) -> None:
        self.exit(result=42, return_code=30, message="Mario")


if __name__ == "__main__":
    app = ExitApp()
    app.run()
    # languages = [
    #     "python", "java", "javascript", "go", "rust",
    #     "haskell", "kotlin", "c#", "sql", "html", "css"
    # ]
    # print("\n".join(languages))

