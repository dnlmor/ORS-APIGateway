from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import requests

# Initialize extensions
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    jwt.init_app(app)

    # Register routes
    from app import routes

    return app
