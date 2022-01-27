"""Initialize Flask Application."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Using a production configuration
    app.config.from_object('config.DevConfig')

    with app.app_context():
        from . import routes

        # Import parts of our application
        from .home import routes

        # Register Blueprints
        # app.register_blueprint(home.home_bp)

        return app
