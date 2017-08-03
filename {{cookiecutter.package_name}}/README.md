# {{cookiecutter.application_name}}

{{cookiecutter.application_name}} description

## Quick Start

Run the application:

    make run

And open it in the browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Prerequisites

This is built to be used with Python 3. Update `Makefile` to switch to Python 2 if needed.

Some Flask dependencies are compiled during installation, so `gcc` and Python header files need to be present.
For example, on Ubuntu:

    apt install build-essential python3-dev


## Development environment and release process

 - create virtualenv with Flask and {{cookiecutter.application_name}} installed into it (latter is installed in
   [develop mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode) which allows
   modifying source code directly without a need to re-install the app): `make venv`

 - run development server in debug mode: `make run`; Flask will restart if source code is modified

 - run tests: `make test`

 - release a production version: `make release` (will run tests first)

 - to remove virtualenv and built distributions: `make clean`

 - to add more python dependencies: add to `install_requires` in `setup.py`

 - to modify configuration in development environment: edit file `settings.cfg`; this is a local configuration file
   and it is *ignored* by Git - make sure to put a proper configuration file to a production environment when
   deploying


## Deployment

Generally the idea is to build a package (`make release`), deliver it to a server (`scp ...`),
install it (`pip install {{cookiecutter.package_name}}.tar.gz`), ensure that configuration file exists and
`{{cookiecutter.package_name.upper()}}_SETTINGS` environment variable points to it, ensure that user has access to the
working directory to create and write log files in it, and finally run a
[WSGI container](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/) with the application.
Most likely it will also run behind a
[reverse proxy](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/#proxy-setups).

Check out [Deploying with Fabric](http://flask.pocoo.org/docs/0.12/patterns/fabric/#fabric-deployment) on one of the
possible ways to automate the deployment.
