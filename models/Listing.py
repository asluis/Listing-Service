from models.shared.db import db

class Listing(db.Model):
    __tablename__ = 'Listings'
    listing_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    tags = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    owner = db.Column(db.String(50), nullable=False)

    def __init__(self, listing_id, title, tags, description, price, owner):
        self.listing_id = listing_id
        self.title = title
        self.tags = tags
        self.description = description
        self.price = price
        self.owner = owner


