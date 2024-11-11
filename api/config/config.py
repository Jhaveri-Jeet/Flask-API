import os

# Base config class
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')  # Default secret key if not found
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')  # Default database URI if not found
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To disable modification tracking
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret')  # Default JWT secret if not found

# Development environment config
class DevelopmentConfig(Config):
    DEBUG = True  # Enable debugging in development

# Production environment config
class ProductionConfig(Config):
    DEBUG = False  # Disable debugging in production

# A dictionary to easily access config classes by environment
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
