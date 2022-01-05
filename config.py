from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes


class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:{config('DB_PORT')}/{config('DB_NAME')}"


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)
    migrate = Migrate(app, db)
    [api.add_resource(*route) for route in routes]
    return app
