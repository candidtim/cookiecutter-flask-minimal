import os

REMOVE_PATHS = [
    '{% if cookiecutter.use_uv == "y" %} Makefile {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
