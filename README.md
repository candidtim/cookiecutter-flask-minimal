# flask-minimal

This is a **minimal** [Flask](http://flask.pocoo.org) project, with no external dependencies except for Flask
itself. It doesn't impose how to implement the web application, but it is **ready for production** deployment from the
start.


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

 - minimal production-ready Flask application: root package, sample static resource, sample template and an index view,
   as per [Larger Applications](http://flask.pocoo.org/docs/0.12/patterns/packages/)

 - setuptools configuration to package and release the application, as well as to develop locally, as per
   [Deploying with Setuptools](http://flask.pocoo.org/docs/0.12/patterns/distribute/)

 - configuration system, as per [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/#config)

 - basic logging configuration, as per [Logging to a File](http://flask.pocoo.org/docs/0.12/errorhandling/#logging-to-a-file)

 - sample test and configuration necessary to run the tests, as per
   [The Testing Skeleton](http://flask.pocoo.org/docs/0.12/testing/#the-testing-skeleton)

 - Makefile with few typical tasks automated (see generated README for details)

Not included:

 - everything else: there is no SQLAlchemy, or MongoKit, or Bootstrap CSS, or React, or whatever else here;
   it is up to you to chose how to implement your application

 - no choice on how to [deploy the application](http://flask.pocoo.org/docs/0.12/deploying/) is made, no WSGI container
   is chosen; if you are interested in an out-of-the-box deployment automation, check out accompanying
   [`cookiecutter-flask-ansible`](https://github.com/candidtim/cookiecutter-flask-ansible); see generated
   README for more ideas about deployment


# Contributions

... are welcome! Feel free to create a pull request to fix bugs or keep up to date.

If you think some additional feature is indispensable, feel free to create an issue or a pull request, but bare in mind
that the goal of this template is to stay a "minimal" one. If you would like to add a feature, maybe best way to do so
is to make it optional and off by default then. One can use cookiecutter's choice variables, and, ultimately, hooks,
in order to create an optional feature.

If you do a change, use `make test` from root directory to test the updated template.


# Attributions

Configuration of this entire project template is based on
[Flask documentation](http://flask.pocoo.org/docs/). Please, note however, that this template is not guaranteed to
follow Flask documentation precisely.


# Possible future improvements

 - add optional configuration for e-mail error reporting and/or Sentry
 - add choice for testng framework (and also make it entirely optional)
 - find a cross-platform replacement to a Makefile
