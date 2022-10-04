from flask import Flask
from flask import render_template
import requests
from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()


def register_extensions(app):
    db.init_app(app)


def create_app():
    application = Flask(__name__)
    # application.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:password@postgres:5432/maindb'

    NAME=os.environ['RDS_DB_NAME']
    USER= os.environ['RDS_USERNAME']
    PASSWORD= os.environ['RDS_PASSWORD']
    HOST= os.environ['RDS_HOSTNAME']
    PORT= os.environ['RDS_PORT']
    application.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
    register_extensions(application)
    return application

application=create_app()

from app import routes,models

with application.app_context():
    db.create_all()
