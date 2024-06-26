from flask import Flask
from .routes import api_gateway_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Register the API Gateway blueprint
    app.register_blueprint(api_gateway_bp)

    return app
