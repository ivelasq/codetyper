"""Custom exceptions for CodeTyper."""


class CodeTyperError(Exception):
    """Base exception for all CodeTyper errors.

    All CodeTyper-specific exceptions inherit from this class,
    making it easy to catch any CodeTyper error.

    Examples
    --------
    >>> try:
    ...     # CodeTyper operations
    ...     pass
    ... except CodeTyperError as e:
    ...     print(f"CodeTyper error: {e}")
    """
    pass


class ConfigurationError(CodeTyperError):
    """Raised when there are configuration or parsing errors.

    This includes:
    - Invalid YAML frontmatter
    - Missing required configuration fields
    - Invalid file formats
    - Unsupported file types

    Examples
    --------
    >>> raise ConfigurationError("Invalid YAML frontmatter")
    """
    pass


class ExecutionError(CodeTyperError):
    """Raised when code execution or IDE operations fail.

    This includes:
    - Code execution failures
    - Positron IDE access issues
    - Missing accessibility permissions
    - File write errors

    Examples
    --------
    >>> raise ExecutionError("Failed to open Positron IDE")
    """
    pass
