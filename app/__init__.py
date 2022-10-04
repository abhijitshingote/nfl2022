from flask import Flask
from flask import render_template
import requests
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


def register_extensions(app):
    db.init_app(app)


def create_app():
    application = Flask(__name__)
    # application.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:password@postgres:5432/maindb'
    application.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg2://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}:{os.environ['RDS_PORT']}/{os.environ['RDS_DB_NAME']}'
    register_extensions(application)
    return application

application=create_app()
with application.app_context():
    db.create_all()
from app import routes


