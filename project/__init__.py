import secrets

from flask import Flask
from flasgger import Swagger
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from .routes import register_routes

SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
SECRET_KEY = "SECRET_KEY"

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(db_uri: str) -> Flask:
    """
    Creates Flask application
    :param db_uri: SQLAlchemy database
    :return: Flask application object
    """
    app = Flask(__name__)
    Swagger(app)
    bcrypt.init_app(app)
    app.config[SECRET_KEY] = secrets.token_hex(16)
    app.config[SQLALCHEMY_DATABASE_URI] = db_uri

    app.json.sort_keys = False

    _init_db(app)
    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import project.models
    with app.app_context():
        db.create_all()