"""CodeTyper - Terminal typewriter effect tool for coding tutorials."""

__version__ = "0.1.0"

from codetyper.config import Config, CodeBlock
from codetyper.exceptions import CodeTyperError, ConfigurationError, ExecutionError

__all__ = [
    "Config",
    "CodeBlock",
    "CodeTyperError",
    "ConfigurationError",
    "ExecutionError",
]
