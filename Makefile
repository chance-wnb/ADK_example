.PHONY: help install install-dev test test-cov format lint type-check clean run-cli run-web sync

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install production dependencies
	uv sync

install-dev:  ## Install development dependencies
	uv sync --extra dev

sync:  ## Sync all dependencies (including dev)
	uv sync --extra dev --extra test

test:  ## Run tests
	uv run pytest

test-cov:  ## Run tests with coverage report
	uv run pytest --cov=math_agent --cov-report=html --cov-report=term-missing

format:  ## Format code with black and isort
	uv run black .
	uv run isort .

lint:  ## Run linting checks
	uv run black --check .
	uv run isort --check-only .

type-check:  ## Run type checking with mypy
	uv run mypy math_agent/

quality:  ## Run all code quality checks
	make lint
	make type-check
	make test

clean:  ## Clean up build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

run-cli:  ## Run the agent in CLI mode
	cd math_agent && uv run adk run .

run-web:  ## Run the agent in web UI mode
	uv run adk web

build:  ## Build the package
	uv build

# Development workflow targets
dev-setup: install-dev  ## Set up development environment
	@echo "✅ Development environment ready!"
	@echo "Run 'make run-cli' to start the agent"

check: format type-check test  ## Run all checks (format, type-check, test)
	@echo "✅ All checks passed!"