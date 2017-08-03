# flask-minimal

This is a **minimal** [Flask](http://flask.pocoo.org) project, with no external dependencies except for Flask
itself. It doesn't impose how to implement the web application, but it is **ready for production** deployment from the
start.


## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    pip install --user cookiecutter

And then, create your application from this template:

    cookiecutter https://github.com/candidtim/cookiecutter-flask-minimal.git

All set! Run the application now:

    cd yourapplication
    make run


## Features

Included:

 - minimal production-ready Flask application: root package, sample static resource, sample template and an index view,
   as per [Larger Applications](http://flask.pocoo.org/docs/0.12/patterns/packages/)

 - setuptools configuration to package and release the application, as well as to develop locally, as per
   [Deploying with Setuptools](http://flask.pocoo.org/docs/0.12/patterns/distribute/)

 - configuration system, as per [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/#config)

 - basic logging configuration, as per [Logging to a File](http://flask.pocoo.org/docs/0.12/errorhandling/#logging-to-a-file)

 - Makefile with few typical tasks automated (see generated README for details)

Not included:

 - everything else: there is no SQLAlchemy, or MongoKit, or Bootstrap CSS, or React, or whatever else here;
   it is up to you to chose how to implement your application

 - no choice on how to [deploy the application](http://flask.pocoo.org/docs/0.12/deploying/) is made, no WSGI container
   is chosen; if you deploy to your own host, make sure to
   [use an WSGI container](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/) instead of Flask development
   server; see generated README for more ideas about deployment

 - no configuration for testing, as there are too many ways to do it and it is a matter of personal choice; check out
   [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/) for a quick start if in doubt


# Attributions

Configuration of this entire project template is based on
[Flask documentation](http://flask.pocoo.org/docs/). Please, note however, that this template is not guaranteed to
follow Flask documentation precisely.


## Possible future improvements

 - create cookicutter template with Ansible project for deployment of projects generated from this template
 - add *optional* (how?) configuration for e-mail logging and/or Sentry (maybe just a Git patch file to apply)
