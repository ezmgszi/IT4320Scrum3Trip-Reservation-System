"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.config["RECAPTCHA_PUBLIC_KEY"] = "iubhiukfgjbkhfvgkdfm"
    app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}

    app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

    with app.app_context():
        # Import parts of our flask_wtforms_tutorial
        from . import routes

        return app
