# PyPkg - Modern Python Package Demo

A modern Python package sample demonstrating standard practices.

## Features

- **Modern Python packaging** with `pyproject.toml`
- **Comprehensive testing** with pytest
- **Code quality tools** with ruff

## Installation

### Using pip (traditional)

```bash
# Install the package
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"
```

### Using uv (recommended)

```bash
# Install uv first
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment
uv venv

# Install the package
uv pip install -e .

# Install with development dependencies
uv pip install -e ".[dev]"
```

## Testing

### Run all tests

```bash
uv run pytest
```

### Development tools

```bash
# Format code check
uv run ruff format --diff pypkg

# Format code
uv run ruff format pypkg

# Check code issues
uv run ruff check pypkg

# Fix auto-fixable issues
uv run ruff check --fix pypkg
```
