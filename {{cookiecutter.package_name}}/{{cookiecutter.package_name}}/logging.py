import logging.config
import os


# Since logging is initialized before the application, can't use
# app.debug here, relying on FLASK_DEBUG env var only.
def _is_debug():
    flag = os.getenv("FLASK_DEBUG", "").lower()
    return flag == "true" or flag == "1"


def init_logging():
    msg_fmt = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": msg_fmt,
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                }
            },
            "root": {
                "level": "DEBUG" if _is_debug() else "INFO",
                "handlers": ["wsgi"],
            },
            "disable_existing_loggers": False,
        }
    )
