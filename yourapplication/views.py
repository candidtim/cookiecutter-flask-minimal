from flask import render_template

from yourapplication import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')
