# Installation Guide

## For Users

### Install from PyPI

```bash
pip install positron-codetyper
```

This is the recommended way to install for everyday use.

### Local Installation

To install from source (e.g. for development):

1. Clone or download this repository
2. Navigate to the codetyper directory
3. Install the package:

```bash
cd codetyper
pip install -e .
```

The `-e` flag installs in "editable" mode, which means you can make changes to the code and they'll take effect immediately.

### Verify Installation

After installation, you should be able to run:

```bash
positron-codetyper --help
```

### Usage

Once installed, use the `positron-codetyper` command instead of `python codetyper.py`:

```bash
# Create a template
positron-codetyper init python -o my_tutorial.py

# Type code in terminal mode
positron-codetyper type-code my_tutorial.py

# Type code in IDE mode
positron-codetyper type-code my_tutorial.py --ide

# With formatting
positron-codetyper type-code my_tutorial.py --format
```

### Uninstall

```bash
pip uninstall positron-codetyper
```

## For Developers

### Development Installation

```bash
# Clone the repository
git clone <repository-url>
cd codetyper

# Install in editable mode with development dependencies
pip install -e .

# Run tests (if any)
python -m pytest tests/
```

### Package Structure

```
codetyper/
├── src/
│   └── positron_codetyper/
│       ├── __init__.py      # Package initialization
│       ├── __main__.py      # python -m positron_codetyper support
│       ├── app.py           # Main application orchestrator
│       ├── cli.py           # Command-line interface
│       ├── config.py        # Configuration dataclasses
│       ├── engine.py        # Typing engines
│       ├── exceptions.py    # Custom exceptions
│       ├── executor.py      # Code execution
│       ├── formatter.py     # Code formatting
│       ├── parser.py        # Config file parsers
│       ├── templates.py     # Script templates
│       └── writer.py        # File writing
├── examples/                # Example scripts
├── tests/                   # Test files
├── pyproject.toml          # Package configuration
├── LICENSE                 # MIT license
└── README.md              # Documentation
```

## Publishing a New Release

To build and publish a new version to PyPI:

```bash
# Build the package
pip install build
python -m build

# Upload to PyPI (requires PyPI account)
pip install twine
twine upload dist/*
```

Users can then install or upgrade with:

```bash
pip install --upgrade positron-codetyper
```
