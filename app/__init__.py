from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


def create_app(config_name):
    app = Flask(__name__)
    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting configuration
    from.requests import configure_request
    configure_request(app)

    return app





