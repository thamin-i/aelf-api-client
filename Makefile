SOURCE_DIR=aelf_client
PYTHON_BIN=.venv/bin/python3
PIP_BIN=.venv/bin/pip
POETRY_BIN=.venv/bin/poetry

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Base commands
install: _setup_dev_env _install_hooks ## Install the local dev environment

uninstall: _clean_dev_env _uninstall_hooks  ## Uninstall the local dev environment

# Development commands
check_code: _ruff_format _isort _mypy _ruff_lint _lint  ## Check the Python source code format, imports, types and lint

format_code:  ## Format the Python source code
	$(PYTHON_BIN) -m ruff format $(SOURCE_DIR)
	$(PYTHON_BIN) -m isort $(SOURCE_DIR)

# Setup commands
_setup_dev_env:
	python3 -m venv .venv
	$(PIP_BIN) install --upgrade pip poetry
	$(POETRY_BIN) install --with dev

# Hooks commands
_install_hooks:
	.hooks/install_hooks.sh -i

_uninstall_hooks:
	.hooks/install_hooks.sh -u

# Clean commands
_clean_dev_env: _uninstall_hooks
	rm -rf .venv

# Development tools
_ruff_format:
	$(PYTHON_BIN) -m ruff format $(SOURCE_DIR) --check --diff

_isort:
	$(PYTHON_BIN) -m isort $(SOURCE_DIR) --check-only --df

_mypy:
	$(PYTHON_BIN) -m mypy $(SOURCE_DIR)

_ruff_lint:
	$(PYTHON_BIN) -m ruff check $(SOURCE_DIR)

_lint:
	export PYTHONPATH="${PYTHONPATH}:$$(pwd)" && $(PYTHON_BIN) -m pylint $(SOURCE_DIR)
