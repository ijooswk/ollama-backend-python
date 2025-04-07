from flask import Flask
from app.routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Register blueprints
    app.register_blueprint(api)

    return app

app = create_app()