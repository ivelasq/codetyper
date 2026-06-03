# Distribution Guide

## Sharing Your Package

### Method 1: GitHub Installation (Recommended for now)

Users can install directly from your GitHub repository:

```bash
pip install git+https://github.com/yourusername/codetyper.git
```

Or from a specific branch:

```bash
pip install git+https://github.com/yourusername/codetyper.git@main
```

### Method 2: Local Distribution

Share the repository as a zip file. Users can then:

```bash
# Unzip the package
unzip codetyper.zip
cd codetyper

# Install locally
pip install -e .
```

### Method 3: Build and Share Wheel

Build a distributable wheel file:

```bash
# Install build tools
pip install build

# Build the package
python -m build

# This creates:
# - dist/codetyper-0.1.0-py3-none-any.whl
# - dist/codetyper-0.1.0.tar.gz
```

Users can install from the wheel:

```bash
pip install codetyper-0.1.0-py3-none-any.whl
```

## Publishing to PyPI (Future)

When ready to publish publicly:

### 1. Create PyPI Account

- Go to https://pypi.org/account/register/
- Create an account and verify email

### 2. Install Twine

```bash
pip install twine
```

### 3. Build the Package

```bash
python -m build
```

### 4. Upload to Test PyPI (Recommended First)

```bash
# Upload to test repository
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ codetyper
```

### 5. Upload to PyPI

```bash
twine upload dist/*
```

### 6. Users Install

Once on PyPI, anyone can install with:

```bash
pip install codetyper
```

## Version Management

Update version in `pyproject.toml`:

```toml
[project]
name = "codetyper"
version = "0.2.0"  # Update this
```

Follow semantic versioning:
- **0.1.0** → **0.1.1**: Bug fixes
- **0.1.0** → **0.2.0**: New features
- **0.1.0** → **1.0.0**: Major changes/breaking changes

## Before Publishing

1. Test thoroughly
2. Update README.md
3. Update CHANGELOG.md (if you create one)
4. Update version in pyproject.toml
5. Create a git tag: `git tag v0.1.0`
6. Push tag: `git push origin v0.1.0`

## Package Metadata

Update `pyproject.toml` before publishing:

```toml
[project]
name = "codetyper"
version = "0.1.0"
description = "Create realistic typing demonstrations for coding tutorials"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["tutorial", "typing", "demo", "screen recording", "education"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

[project.urls]
Homepage = "https://github.com/yourusername/codetyper"
Documentation = "https://github.com/yourusername/codetyper#readme"
Repository = "https://github.com/yourusername/codetyper"
"Bug Tracker" = "https://github.com/yourusername/codetyper/issues"
```
