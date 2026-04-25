from flask import Blueprint, render_template
from flask import current_app as app

bp = Blueprint("root", __name__)


@bp.route("/")
def index():
    app.logger.warning("sample message")
    return render_template("index.html")
