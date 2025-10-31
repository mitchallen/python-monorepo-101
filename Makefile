.PHONY: help setup install test lint format clean run-api coverage coverage-report coverage-html coverage-open

# Default target
help:
	@echo "Available commands:"
	@echo "  make setup           - Install all dependencies"
	@echo "  make install         - Alias for setup"
	@echo "  make test            - Run tests"
	@echo "  make coverage        - Run tests with coverage report"
	@echo "  make coverage-html   - Generate HTML coverage report"
	@echo "  make coverage-open   - Generate HTML coverage report and open in browser"
	@echo "  make coverage-report - Show coverage summary"
	@echo "  make lint            - Run linter (ruff)"
	@echo "  make format          - Format code (ruff format)"
	@echo "  make clean           - Clean build artifacts"
	@echo "  make run-api         - Run example API demo"

# Install all dependencies
setup install:
	uv sync

# Run tests
test:
	uv run pytest tests/ -v

# Run tests with coverage
coverage:
	uv run pytest tests/ -v --cov=packages --cov-report=term-missing

# Generate HTML coverage report
coverage-html:
	uv run pytest tests/ --cov=packages --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

# Generate HTML coverage report and open in browser
coverage-open: coverage-html
	@echo "Opening coverage report in browser..."
	@open htmlcov/index.html 2>/dev/null || xdg-open htmlcov/index.html 2>/dev/null || start htmlcov/index.html 2>/dev/null || echo "Please open htmlcov/index.html manually in your browser"

# Show coverage summary
coverage-report:
	uv run pytest tests/ --cov=packages --cov-report=term-missing --cov-report= | tail -n +5

# Run linter
lint:
	uv run ruff check .

# Format code
format:
	uv run ruff format .

# Clean build artifacts
clean:
	rm -rf .venv
	rm -rf **/__pycache__
	rm -rf **/.pytest_cache
	rm -rf **/dist
	rm -rf **/*.egg-info
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Run example API demo
run-api:
	@echo "Running API demo..."
	@uv run python -c "from api import PaymentService, UserService; ps = PaymentService(); print('Payment:', ps.calculate_total(100, 0.1)); us = UserService(); print('User validation:', us.validate_user('test@example.com', '555-1234'))"

