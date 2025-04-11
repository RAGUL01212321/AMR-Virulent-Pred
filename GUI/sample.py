from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input
from textual.containers import Vertical
from textual.reactive import reactive
from pathlib import Path

class AMRApp(App):

    CSS_PATH = None  # Optional: set if using CSS styling
    file_path = reactive("No file selected.")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("🧬 AMR 1.0 - Gene Predictor", classes="title"),
            Button("Upload DNA Sequence", id="upload"),
            Static(self.file_path, id="filepath"),
            Button("Predict", id="predict", variant="success"),
            id="main-panel"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "upload":
            file = self.pick_file()
            if file:
                self.file_path = str(file)
                self.query_one("#filepath", Static).update(f"Selected file:\n{file}")
        elif event.button.id == "predict":
            if "No file" in self.file_path:
                self.bell()
            else:
                # Call your model logic here
                self.query_one("#filepath", Static).update(f"Predicting on:\n{self.file_path}")

    def pick_file(self):
        """Dummy file picker using input for now (TUI can't show native dialogs)."""
        print("\nEnter the path to your DNA sequence file:")
        path = input("> ").strip()
        return Path(path) if Path(path).exists() else None

if __name__ == "__main__":
    app = AMRApp()
    app.run()
