all: test

clean:
	rm -rf /tmp/yourapplication/

test: clean
	cookiecutter . --output-dir /tmp --replay --replay-file test-config.json && \
	cd /tmp/yourapplication && \
	poetry run pytest && \
	poetry run black --check . && \
	poetry run isort --check . && \
	poetry run flake8 . && \
	poetry run mypy
