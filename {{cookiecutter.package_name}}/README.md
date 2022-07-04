# {{cookiecutter.application_name}}

{{cookiecutter.application_name}} description

## Quick Start

Run the application:

    make run

And open it in the browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Prerequisites

Python >=3.7

## Development environment

 - `make venv`: creates a virtualenv with dependencies and this application
   installed (latter is installed in [development mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode))

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

 - `make test`: runs tests (see also: [Testing Flask Applications](https://flask.palletsprojects.com/en/2.1.x/testing/))

 - `make dist`: creates a wheel distribution (will run tests first)

 - `make clean`: removes virtualenv and build artifacts

 - add application dependencies in `pyproject.toml` under `project.dependencies`;
   add development dependencies under `project.optional-dependencies.*`

 - to modify configuration, pass it in environment variables prefixed with
   `FLASK_`; e.g., `FLASK_DEBUG`, etc.;

## Configuration

Default configuration is loaded from `{{cookiecutter.package_name}}.default_settings` and can be
overriden by environment variables with a `FLASK_` prefix. See
[Configuring from Environment Variables](https://flask.palletsprojects.com/en/2.1.x/config/#configuring-from-environment-variables).

Consider using
[dotenv](https://flask.palletsprojects.com/en/2.1.x/cli/#environment-variables-from-dotenv).

## Deployment

See [Deploying to Production](https://flask.palletsprojects.com/en/2.1.x/deploying/).

You may use the distribution (`make dist`) to publish it to a package index,
deliver to your server, or copy in your `Dockerfile`, and insall it with `pip`.

You must set a
[SECRET_KEY](https://flask.palletsprojects.com/en/2.1.x/tutorial/deploy/#configure-the-secret-key)
in production to a secret and stable value.
