"""CodeTyper - Terminal typewriter effect tool for coding tutorials."""

__version__ = "0.1.0"

from positron_codetyper.config import Config, CodeBlock
from positron_codetyper.exceptions import CodeTyperError, ConfigurationError, ExecutionError

__all__ = [
    "Config",
    "CodeBlock",
    "CodeTyperError",
    "ConfigurationError",
    "ExecutionError",
]
