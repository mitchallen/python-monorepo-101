# Python Monorepo Demo

A demonstration Python monorepo using `uv` for package management and `make` for task automation.

## Structure

This monorepo contains three packages:

- **core**: Basic calculator functionality
- **utils**: Utility functions (formatters, validators) that depend on `core`
- **api**: API services that depend on both `core` and `utils`

```
.
├── packages/
│   ├── core/          # Core package
│   ├── utils/         # Utilities package (depends on core)
│   └── api/           # API package (depends on core and utils)
├── tests/             # Test files
├── Makefile           # Task automation
├── pyproject.toml     # Workspace configuration
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) installed
- `make` (usually pre-installed on Unix systems)

### Installing uv

If you don't have `uv` installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Getting Started

1. **Install dependencies:**
   ```bash
   make setup
   ```
   or
   ```bash
   uv sync
   ```

2. **Run the example:**
   ```bash
   make run-api
   ```

## Available Commands

- `make setup` - Install all dependencies
- `make test` - Run tests
- `make coverage` - Run tests with coverage report
- `make coverage-html` - Generate HTML coverage report (saves to `htmlcov/index.html`)
- `make coverage-open` - Generate HTML coverage report and open in browser
- `make coverage-report` - Show coverage summary
- `make lint` - Run linter (ruff)
- `make format` - Format code (ruff format)
- `make clean` - Clean build artifacts
- `make run-api` - Run example API demo

## Package Dependencies

```
api
├── core
└── utils
    └── core
```

## Adding New Packages

1. Create a new directory under `packages/`
2. Initialize it with `uv init` or manually create `pyproject.toml`
3. Add dependencies to other packages using:
   ```toml
   dependencies = [
       "package-name",
   ]
   
   [tool.uv.sources]
   package-name = { path = "../package-name", editable = true }
   ```
4. Run `uv sync` to update the workspace

## Code Coverage

This project includes code coverage support using `pytest-cov`. You can:

- Run tests with coverage: `make coverage`
- Generate HTML coverage report: `make coverage-html` (saves to `htmlcov/index.html`)
- Generate and open HTML coverage report in browser: `make coverage-open`
- View coverage summary: `make coverage-report`

Coverage configuration is defined in `pyproject.toml` and excludes test files and common patterns like `__repr__` methods.

## Development

All packages are installed in editable mode, so changes to source code take effect immediately after saving.

