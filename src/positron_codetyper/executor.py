"""Code execution functionality."""

import subprocess
from typing import Tuple

from rich.console import Console
from rich.panel import Panel


class CodeExecutor:
    """Executes R or Python code blocks."""

    def __init__(self, language: str):
        self.language = language
        self.console = Console()

    def execute_block(self, code: str) -> Tuple[str, str, int]:
        """Execute code and return (stdout, stderr, returncode)."""
        try:
            if self.language == 'r':
                result = subprocess.run(
                    ["Rscript", "--quiet", "-e", code],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
            elif self.language == 'python':
                result = subprocess.run(
                    ["python3", "-c", code],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
            else:
                return "", f"Unknown language: {self.language}", 1

            return result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired:
            return "", "Execution timed out (30s limit)", 1
        except FileNotFoundError as e:
            return "", f"Command not found: {e}", 1
        except Exception as e:
            return "", str(e), 1

    def display_output(self, stdout: str, stderr: str, returncode: int):
        """Display execution results with Rich formatting."""
        if returncode == 0:
            if stdout.strip():
                self.console.print(Panel(
                    stdout,
                    title="Output",
                    border_style="green"
                ))
        else:
            if stderr.strip():
                self.console.print(Panel(
                    stderr,
                    title="Error",
                    border_style="red"
                ))
