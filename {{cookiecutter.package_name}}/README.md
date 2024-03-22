# {{cookiecutter.application_name}}

{{cookiecutter.application_name}} description

## Quick Start
{%- if cookiecutter.use_poetry == 'y' %}

Install the dependencies and run the application:

    poetry install
    poetry run flask --debug run
{%- else %}

Run the application:

    make run
{%- endif %}

And open it in the browser at [http://localhost:5000/](http://localhost:5000/)

## Prerequisites

Python >=3.8

## Development environment
{%- if cookiecutter.use_poetry == 'y' %}

This project uses [Poetry](https://python-poetry.org/docs/).

Quick start:

    poetry install

    poetry run pytest
    {%- if cookiecutter.use_black == 'y' %}
    poetry run black [--check] .{%- endif %}
    {%- if cookiecutter.use_isort == 'y' %}
    poetry run isort [--check] .{%- endif %}
    {%- if cookiecutter.use_flake8 == 'y' %}
    poetry run flake8 .{% endif %}
    {%- if cookiecutter.use_mypy == 'y' %}
    poetry run mypy{% endif %}

Run a development server in debug mode (changes in are reloaded automatically):

    poetry run flask --app {{cookiecutter.package_name}} --debug run
{%- else %}

 - `make venv`: creates a virtualenv with dependencies and this application
   installed in [development mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode)

 - `make run`: runs a development server in debug mode (changes in source code
   are reloaded automatically)

{%- if cookiecutter.use_black == 'y' %}

 - `make format`: reformats code
{%- endif %}
{%- if cookiecutter.use_flake8 == 'y' %}

 - `make lint`: runs flake8
{%- endif %}
{%- if cookiecutter.use_mypy == 'y' %}

 - `make mypy`: runs type checks by mypy
{%- endif %}

 - `make test`: runs tests (see also: [Testing Flask Applications](https://flask.palletsprojects.com/en/3.0.x/testing/))

 - `make dist`: creates a wheel distribution (will run tests first)

 - `make clean`: removes virtualenv and build artifacts

 - add application dependencies in `pyproject.toml` under `project.dependencies`;
   add development dependencies under `project.optional-dependencies.*`; run
   `make clean && make venv` to reinstall the environment
{%- endif %}

## Configuration

Default configuration is loaded from `{{cookiecutter.package_name}}.defaults` and can be
overriden by environment variables with a `FLASK_` prefix. See
[Configuring from Environment Variables](https://flask.palletsprojects.com/en/3.0.x/config/#configuring-from-environment-variables).

Consider using
[dotenv](https://flask.palletsprojects.com/en/3.0.x/cli/#environment-variables-from-dotenv).

## Deployment

See [Deploying to Production](https://flask.palletsprojects.com/en/3.0.x/deploying/).

You may use the distribution (`make dist`) to publish it to a package index,
deliver to your server, or copy in your `Dockerfile`, and insall it with `pip`.

You must set a
[SECRET_KEY](https://flask.palletsprojects.com/en/3.0.x/tutorial/deploy/#configure-the-secret-key)
in production to a secret and stable value.
