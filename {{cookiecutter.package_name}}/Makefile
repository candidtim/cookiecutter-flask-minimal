all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run: venv
	FLASK_APP={{cookiecutter.package_name}} {{cookiecutter.package_name.upper()}}_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	{{cookiecutter.package_name.upper()}}_SETTINGS=../settings.cfg venv/bin/python tests/test_{{cookiecutter.package_name}}.py

release: venv test
	venv/bin/python setup.py sdist
