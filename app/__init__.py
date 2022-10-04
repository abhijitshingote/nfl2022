from flask import Flask
from flask import render_template
import requests
# from flask_sqlalchemy import SQLAlchemy

# db=SQLAlchemy()


# def register_extensions(app):
#     db.init_app(app)


def create_app():
    application = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:password@postgres:5432/maindb'
    # register_extensions(app)
    return application

application=create_app()
# with app.app_context():
#     db.create_all()
from app import routes
