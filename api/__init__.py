from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from api.config.config import config
from dotenv import load_dotenv
import os
import pymysql


# Initialize global instances of db and jwt
pymysql.install_as_MySQLdb()
db = SQLAlchemy()
jwt = JWTManager()

def createApp(configuration="development"):
    """
    Factory function to create and initialize the Flask app.
    """

    # Initialize the Flask app
    app = Flask(__name__)

    # Configuring the app with settings from the config.py based on the environment
    app.config.from_object(config[configuration])

    # Load environment variables from the .env file
    load_dotenv()

    # Initialize extensions with the Flask app
    db.init_app(app)
    jwt.init_app(app)

    # Set app-level configuration for sensitive data like SECRET_KEY
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')  # Fallback to default if not found
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')  # Fallback to SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret')  # Default value for JWT

    # Register routes with app
    from api.routes.userRoutes import userBp
    app.register_blueprint(userBp, url_prefix='/user')

    return app
