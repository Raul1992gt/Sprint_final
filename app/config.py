import os


class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "postgresql://sprint_final:sprint_final@database:5432/sprint_final")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration variables as needed


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # Add other production configurations here

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # Usa una base de datos en memoria para pruebas


# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig 
    # Add other environments if needed
}
