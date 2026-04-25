all: test

clean:
	rm -rf /tmp/yourapplication/

test-uv:
	rm -rf /tmp/yourapplication/ && \
	cookiecutter . --output-dir /tmp --replay --replay-file test-config-uv.json && \
	cd /tmp/yourapplication && \
	uv lock && \
	uv sync && \
	uv run pytest && \
	uv run ruff check && \
	uv run ruff format --check && \
	uv run mypy

test-setuptools:
	rm -rf /tmp/yourapplication/ && \
	cookiecutter . --output-dir /tmp --replay --replay-file test-config-setuptools.json && \
	cd /tmp/yourapplication && \
	make venv && \
	make test && \
	make lint && \
	make mypy

test: test-uv test-setuptools
