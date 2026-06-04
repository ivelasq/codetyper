"""Code formatting functionality."""

import subprocess

from rich.console import Console


class CodeFormatter:
    """Formats code files after typing completes."""

    def __init__(self, language: str):
        self.language = language
        self.console = Console()

    def format_file(self, file_path: str) -> bool:
        """Format the code file. Returns True if successful."""
        try:
            if self.language == 'python':
                return self._format_python(file_path)
            elif self.language == 'r':
                return self._format_r(file_path)
            else:
                return False
        except Exception as e:
            self.console.print(f"[yellow]Warning: Could not format file: {e}[/yellow]")
            return False

    def _format_python(self, file_path: str) -> bool:
        """Format Python file with Ruff."""
        try:
            check_commands = [
                ['ruff', '--version'],
                ['python', '-m', 'ruff', '--version'],
            ]

            ruff_cmd = None
            for cmd in check_commands:
                try:
                    result = subprocess.run(cmd,
                                          capture_output=True,
                                          text=True,
                                          timeout=5)
                    if result.returncode == 0:
                        ruff_cmd = cmd[:-1]
                        break
                except (FileNotFoundError, subprocess.TimeoutExpired):
                    continue

            if not ruff_cmd:
                self.console.print("[dim]Ruff not found - skipping formatting[/dim]")
                return False

            format_cmd = ruff_cmd + ['format', file_path]
            result = subprocess.run(format_cmd,
                                  capture_output=True,
                                  text=True,
                                  timeout=10)

            if result.returncode == 0:
                self.console.print("[green]✓ Formatted with Ruff[/green]")
                return True
            else:
                self.console.print(f"[yellow]Ruff formatting failed: {result.stderr}[/yellow]")
                return False

        except FileNotFoundError:
            self.console.print("[dim]Ruff not installed - skipping formatting[/dim]")
            return False
        except subprocess.TimeoutExpired:
            self.console.print("[yellow]Ruff formatting timed out[/yellow]")
            return False

    def _format_r(self, file_path: str) -> bool:
        """Format R file with styler."""
        try:
            check_cmd = 'Rscript -e "if (!require(styler, quietly=TRUE)) quit(status=1)"'
            result = subprocess.run(check_cmd,
                                  shell=True,
                                  capture_output=True,
                                  text=True)

            if result.returncode != 0:
                self.console.print("[dim]styler package not found - skipping formatting[/dim]")
                return False

            format_cmd = f'Rscript -e "styler::style_file(\'{file_path}\')"'
            result = subprocess.run(format_cmd,
                                  shell=True,
                                  capture_output=True,
                                  text=True,
                                  timeout=10)

            if result.returncode == 0:
                self.console.print("[green]✓ Formatted with styler[/green]")
                return True
            else:
                self.console.print(f"[yellow]styler formatting failed: {result.stderr}[/yellow]")
                return False

        except FileNotFoundError:
            self.console.print("[dim]Rscript not found - skipping formatting[/dim]")
            return False
        except subprocess.TimeoutExpired:
            self.console.print("[yellow]styler formatting timed out[/yellow]")
            return False
