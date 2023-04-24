from flask_sqlalchemy import SQLAlchemy
from main import db

class Listing(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))

