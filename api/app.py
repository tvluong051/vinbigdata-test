import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    stage = os.getenv("STAGE", "development")
    app.config.from_object(config[stage])

    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
