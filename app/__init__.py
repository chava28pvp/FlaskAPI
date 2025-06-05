# app/__init__.py
from flask import Flask
from flasgger import Swagger
from .routes.user_routes import user_bp
from .routes.task_routes import task_bp
from .config import SWAGGER_CONFIG



def create_app():
    app = Flask(__name__)
    Swagger(app, config=SWAGGER_CONFIG)

    app.register_blueprint(user_bp)
    app.register_blueprint(task_bp)

    return app
