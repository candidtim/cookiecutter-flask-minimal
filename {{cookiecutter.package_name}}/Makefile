all: run

clean:
	rm -rf venv build dist .pytest_cache .mypy_cache *.egg-info

venv:
	python3 -m venv venv && \
		venv/bin/pip install --upgrade pip setuptools && \
		venv/bin/pip install --editable ".[tests]"

run: venv
	FLASK_APP={{cookiecutter.package_name}} FLASK_ENV=development venv/bin/flask run

test: venv
	FLASK_ENV=development venv/bin/pytest

dist: venv test
	venv/bin/pip wheel --wheel-dir dist --no-deps .
