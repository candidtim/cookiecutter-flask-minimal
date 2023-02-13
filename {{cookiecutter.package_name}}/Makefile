all: run

clean:
	rm -rf venv build dist .pytest_cache .mypy_cache *.egg-info

venv:
	python3 -m venv venv && \
		venv/bin/pip install --upgrade pip setuptools && \
		venv/bin/pip install --editable ".[dev]"

run: venv
	venv/bin/flask --app {{cookiecutter.package_name}} --debug run

{%- if cookiecutter.use_black == 'y' %}

format: venv
	venv/bin/black .{%- if cookiecutter.use_isort == 'y' %} && venv/bin/isort .{% endif %}

format-check: venv
	venv/bin/black --check .{%- if cookiecutter.use_isort == 'y' %} && venv/bin/isort --check .{% endif %}
{%- endif %}
{%- if cookiecutter.use_flake8 == 'y' %}

lint: venv
	venv/bin/flake8 .
{%- endif %}
{%- if cookiecutter.use_mypy == 'y' %}

mypy: venv
	venv/bin/mypy
{%- endif %}

test: venv
	venv/bin/pytest

dist: venv {% if cookiecutter.use_black == 'y' %}format-check {% endif %}{% if cookiecutter.use_flake8 == 'y' %}lint {% endif %}{% if cookiecutter.use_mypy == 'y' %}mypy {% endif %}test
	venv/bin/pip wheel --wheel-dir dist --no-deps .
