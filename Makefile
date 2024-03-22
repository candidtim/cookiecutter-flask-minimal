all: test

clean:
	rm -rf /tmp/yourapplication/

test: clean
	cookiecutter . --output-dir /tmp --replay --replay-file test-config.json && \
	cd /tmp/yourapplication && \
	poetry run pytest
