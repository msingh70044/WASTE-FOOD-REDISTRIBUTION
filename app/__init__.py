import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
app = Flask(
    __name__,
    static_folder=static_dir,
    static_url_path='/static',
    template_folder='templates'
)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import routes, models

with app.app_context():
    db.create_all()