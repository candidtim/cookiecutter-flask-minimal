.PHONY: all clean venv run format lint mypy test dist

all: run

clean:
	rm -rf .venv build dist {% if cookiecutter.use_ruff == 'y' %}.ruff_cache {% endif %}.pytest_cache {% if cookiecutter.use_mypy == 'y' %}.mypy_cache {% endif %}*.egg-info

.venv:
	python3 -m venv .venv && \
		.venv/bin/pip install --upgrade pip setuptools && \
		.venv/bin/pip install --editable ".[dev]"

venv: .venv

run: venv
	.venv/bin/flask --app {{cookiecutter.package_name}} --debug run
{%- if cookiecutter.use_ruff == 'y' %}

format: venv
	.venv/bin/ruff format
	.venv/bin/ruff check --fix --extend-select=I

lint: venv
	.venv/bin/ruff check --extend-select=I
	.venv/bin/ruff format --check
{%- endif %}
{%- if cookiecutter.use_mypy == 'y' %}

mypy: venv
	.venv/bin/mypy
{%- endif %}

test: venv
	.venv/bin/pytest

dist: venv {% if cookiecutter.use_ruff == 'y' %}lint {% endif %}{% if cookiecutter.use_mypy == 'y' %}mypy {% endif %}test
	.venv/bin/pip wheel --wheel-dir dist --no-deps .
