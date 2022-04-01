from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import crawler
    app.register_blueprint(crawler.blueprint)

    return app
