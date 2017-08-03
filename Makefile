all: run

clean:
	rm -rf .venv && rm -rf *.egg-info && rm -rf dist

venv:
	virtualenv --python=python3 .venv && .venv/bin/python setup.py develop

run:
	FLASK_APP=yourapplication yourapplication_SETTINGS=../settings.cfg .venv/bin/flask run

release:
	.venv/bin/python setup.py sdist
