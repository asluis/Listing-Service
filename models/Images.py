from models.shared import db

class Images(db.Model):
    __tablename__ = 'Images'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    listing_id = db.Column(db.Integer)
    data = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    def __init__(self, image_id: int, listing_id: int, data: str, mimetype: str):
        self.image_id = image_id
        self.listing_id = listing_id
        self.data = data
        self.mimetype = mimetype