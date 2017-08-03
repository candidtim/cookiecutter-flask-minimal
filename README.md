# yourapplication

This is a **minimal** [Flask](http://flask.pocoo.org) project, with no external dependencies except for Flask
itself. It doesn't impose how to implement the web application, but it is **ready for production** deployment from the
start.

Included:

 - minimal production-ready Flask application: root package, sample static resource, sample template and an index view,
   as per [Larger Applications](http://flask.pocoo.org/docs/0.12/patterns/packages/)

 - setuptools configuration to package and release the application, as well as to develop locally, as per
   [Deploying with Setuptools](http://flask.pocoo.org/docs/0.12/patterns/distribute/)

 - configuration system, as per [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/#config)

 - basic logging configuration, as per [Logging to a File](http://flask.pocoo.org/docs/0.12/errorhandling/#logging-to-a-file)

 - Makefile with few typical tasks automated (see below for details)

Not included:

 - everything else: there is no SQLAlchemy, or MongoKit, or Bootstrap CSS, or React, or whatever else here;
   it is up to you to chose how to implement your application

 - no choice on how to [deploy the application](http://flask.pocoo.org/docs/0.12/deploying/) is made, no WSGI container
   is chosen; if you deploy to your own host, make sure to
   [use an WSGI container](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/) instead of Flask development
   server; see below for more ideas about deployment

 - no configuration for testing, as there are too many ways to do it and it is a matter of personal choice; check out
   [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/) for a quick start if in doubt


## Dependencies

This is built to be used with Python 3. Update `Makefile` to switch to Python 2 if needed.

Some Flask dependencies are compiled during installation, so `gcc` and Python header files need to be present.
For example, on Ubuntu:

    apt install build-essential python3-dev


## Development environment and release process

 - create virtualenv with Flask and yourapplication installed into it (latter is installed in
   [develop mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode) which allows
   modifying source code directly without a need to re-install the app): `make venv`

 - run development server in debug mode: `make run`; Flask will restart if source code is modified

 - release a production version: `make release`

 - to remove virtualenv and built distributions: `make clean`

 - to add more python dependencies: add to `install_requires` in `setup.py`

 - to modify configuration in development environment: edit file `settings.cfg`; this is a local configuration file
   and it is *ignored* by Git - make sure to put a proper configuration file to a production environment when
   deploying


## Deployment

Generally the idea is to build a package (`make release`), deliver it to a server (`scp ...`),
install it (`pip install yourapplication.tar.gz`), ensure that configuration file exists and
`yourapplication_SETTINGS` environment variable points to it, ensure that user has access to the
working directory to create and write log files in it, and finally run a
[WSGI container](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/) with the application.
Most likely it will also run behind a
[reverse proxy](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/#proxy-setups).

Check out [Deploying with Fabric](http://flask.pocoo.org/docs/0.12/patterns/fabric/#fabric-deployment) on one of the
possible ways to automate the deployment.


# Attributions

Configuration of this entire project template is based on
[Flask documentation](http://flask.pocoo.org/docs/). Please, note however, that this template is not guaranteed to
follow Flask documentation precisely.


## TODOs

 - TODO: patchfile to add e-mail logging and/or Sentry
 - TODO: create sample project with Ansible for deployment
