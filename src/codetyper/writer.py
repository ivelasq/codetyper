"""File writing functionality."""

from pathlib import Path

from rich.console import Console


class FileWriter:
    """Manages writing typed code to output file."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.file_handle = None

    def open(self):
        """Open file for writing."""
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.file_handle = open(self.filepath, 'w')

    def write_chunk(self, text: str):
        """Append text to output file."""
        if self.file_handle:
            self.file_handle.write(text)
            self.file_handle.flush()

    def close(self):
        """Close file."""
        if self.file_handle:
            self.file_handle.close()

    def finalize(self, console: Console):
        """Close file and display completion message."""
        self.close()
        console.print(f"\n[green]✓[/green] File saved to: {self.filepath}")
