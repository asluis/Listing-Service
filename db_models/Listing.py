from flask_sqlalchemy import SQLAlchemy
from main import db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    tags = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    images = db.Column(db.LargeBinary, nullable=True)
    owner = db.Column(db.String(50), nullable=False)


