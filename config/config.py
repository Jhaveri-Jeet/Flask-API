import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret')

class DevelopmentConfig(Config):
    DEBUG: True

class ProductionConfig(Config):
    DEBUG: False

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}