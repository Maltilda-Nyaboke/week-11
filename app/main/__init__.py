from flask import Flask
from flask_bootstrap import Bootstrap
from flask import Blueprint
from config import config_options

main = Blueprint('main',__name__)
from . import views,errors

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__instance_relative_config = True)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app