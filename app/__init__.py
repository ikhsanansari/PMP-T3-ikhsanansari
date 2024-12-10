from flask import Flask
from app.routes.main_routes import main_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    return app
