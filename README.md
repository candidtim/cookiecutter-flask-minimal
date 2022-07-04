# cookiecutter-flask-minimal

*A microtemplate for a microframework.*

This is a **minimalist's** **production-ready** [Flask](http://flask.pocoo.org) project template:

 - no external dependencies except for [Flask](http://flask.pocoo.org) and [pytest](https://pytest.org)
 - doesn't impose any choices of third-party libraries
 - project set-up as per Flask documentation, including things like logging and config, testing and packaging
 - optional and off by deafult: flake8, black and mypy configuration
 - preserves the pure joy of developing with Flask!

**Now upgraded to Flask 2 !**

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
   an [application factory](https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/),
   and a single [blueprint](https://flask.palletsprojects.com/en/2.1.x/blueprints/)
   with a sample static resource, template and an index view, packaged as as per
   [Larger Applications](https://flask.palletsprojects.com/en/2.1.x/patterns/packages/)

 - setuptools configuration to package and release the application, as well as
   to develop locally, as per
   [Deploying with Setuptools](https://flask.palletsprojects.com/en/2.1.x/patterns/distribute/)

 - configuration system, as per
   [Configuration Handling](https://flask.palletsprojects.com/en/2.1.x/config/)

 - basic [Logging](https://flask.palletsprojects.com/en/2.1.x/logging/) configuration

 - sample test and testing set-up, as per
   [Testing Flask Applications](https://flask.palletsprojects.com/en/2.1.x/testing/)

 - optional (and off by deafult) configuration for flake8, black and mypy

 - Makefile with a few typical tasks automated (see generated README for details)

Not included:

 - everything else: there is no SQLAlchemy, or MongoKit, or Bootstrap CSS, or
   React, or whatever else; it is up to you to chose how to implement your
   application;
   [Patterns for Flask](https://flask.palletsprojects.com/en/2.1.x/patterns/)
   documents well how to easily add these if necessary

 - there are no "sample" features or examples of how to use Flask; this
   template is not intended as a tutorial, but as a well-configured starting
   point for a new implementation; refer to the
   [Flask documentation](https://flask.palletsprojects.com/en/2.1.x/quickstart/)
   to learn Flask if necessary

 - no choice on how to deploy the application is made, no WSGI container is
   chosen; see
   [Deploying to Production](https://flask.palletsprojects.com/en/2.1.x/deploying/)
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
[Flask documentation](https://flask.palletsprojects.com/en/2.1.x/).
Please, note however, that this template is not guaranteed to follow Flask
documentation precisely.
