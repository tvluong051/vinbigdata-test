import os

class Config:
    DEBUG = False
    DEVELOPMENT = False
    PORT = os.getenv("PORT", 5151)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class TestConfig(DevConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

config = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig,
}