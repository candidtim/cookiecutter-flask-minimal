# cookiecutter-flask-minimal

*A microtemplate for a microframework.*

This is a **minimalist's** **production-ready** [Flask](https://flask.palletsprojects.com) project template:

 - zero bloat
 - no dependencies except for [Flask](https://flask.palletsprojects.com) and [pytest](https://pytest.org)
 - complete project set-up as per Flask documentation, including things like logging, configuration, testing and packaging
 - preserves the pure joy of developing with Flask!

Also includes these recommended, but fully **optional** features:

 - [uv](https://docs.astral.sh/uv/) package manager (otherwise the project uses traditional setuptools)
 - [ruff](https://astral.sh/ruff)
 - [mypy](https://www.mypy-lang.org)

**Up to date with Flask 3 !**

A few older configurations are available, but not actively supported:

 - for **Flask 2** check out the `flask2` branch, it is last known to work with Flask 2.3.3
 - for **Poetry**, **flake8**, **black** and **isort** configurations check out
   the `poetry` branch, last known to work with Flask 3.0.2 and Poetry 1.x.

## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    pip install --user cookiecutter

Create your application from this template:

    cookiecutter https://github.com/candidtim/cookiecutter-flask-minimal.git

All set! Run the application:

    cd yourapplication
    make run

And then open it at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Features

Included:

 - minimal production-ready Flask application:
   an [application factory](https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/),
   and a single [blueprint](https://flask.palletsprojects.com/en/3.0.x/blueprints/)
   with a sample static resource, template and an index view, packaged as as per
   [Larger Applications](https://flask.palletsprojects.com/en/3.0.x/patterns/packages/)

 - configuration system, as per
   [Configuration Handling](https://flask.palletsprojects.com/en/3.0.x/config/)

 - basic [Logging](https://flask.palletsprojects.com/en/3.0.x/logging/) configuration

 - sample test and testing set-up, as per
   [Testing Flask Applications](https://flask.palletsprojects.com/en/3.0.x/testing/)

 - `setuptools` or `uv` development environment configuration, including a way
   to package and release the application

 - optional, yet highly recommended, configuration for `ruff` and `mypy`

 - well-documented development environment (see the generated `README.md`)

Not included:

 - everything else: there is no SQLAlchemy, MongoKit, Bootstrap CSS, React, or
   anything else; it is up to you to chose how to implement your application;
   [Patterns for Flask](https://flask.palletsprojects.com/en/3.0.x/patterns/)
   documents well how to easily add these if necessary

 - there are no "sample" features or examples of how to use Flask; this
   template is not intended as a tutorial, but as a well-configured starting
   point for a new implementation; refer to the
   [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
   to learn Flask if necessary

 - no choice on how to deploy the application is made, no WSGI container is
   chosen; see
   [Deploying to Production](https://flask.palletsprojects.com/en/3.0.x/deploying/)
   for the options most suitable for your infrastructure

# Contributions

... are welcome! Feel free to create a pull request to fix bugs or keep up to date.

If you think some additional feature is indispensable, feel free to create an
issue or a pull request, but bare in mind that the goal of this template is to
stay a "minimal" one. If you would like to add a feature, maybe best way to do
so is to make it optional and off by default then. One can use cookiecutter's
choice variables, and, ultimately, hooks, in order to create an optional
feature.

If you do a change, use `make test` from root directory to test the updated template.

# Attributions

Configuration of this entire project template is based on
[Flask documentation](https://flask.palletsprojects.com/en/3.0.x/).
Please, note however, that this template is not guaranteed to follow Flask
documentation precisely.
