def create_app(config_name):

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting configuration
    from.requests import configure_request
    configure_request(app)

    return app





