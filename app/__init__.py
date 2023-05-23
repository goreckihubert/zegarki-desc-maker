from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from config import Config

db = SQLAlchemy()
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    babel.init_app(app)

    from app import routes, models

    return app
