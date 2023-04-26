from flask import Flask, Response
from flask import request
from sqlalchemy.exc import DatabaseError, DataError, IntegrityError
from models.Listing import Listing
from models.shared.db import db, db_init
from flask import jsonify

app = Flask(__name__)


'''
DB Username is UniPal
DB Password is Listing
DB name is UniPal_Listing

Please configure MySQL if needed to meet these requirements by creating the appropriate user and granting access.

Go to setup folder to see the SQL script that does all of this for you.
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://UniPal:Listing@localhost/UniPal_Listing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/api/v1/')
def main() -> Response:
    return jsonify({'success': True,
                    'response': "This is University Pal's Listing microservice for everything related to a listing."})

# Creates a listing. Requires that ALL parameters have a value.
@app.route('/api/v1/create/<uid>/<title>/<price>/<desc>/<images>/<tags>', methods=['POST'])
def create_listing(uid: str = None, title: str = None, price: float = 0.00, desc: str = "", images: str = None,
                   tags: str = None) -> Response:
    if uid is None or title is None or price is None or desc is None or images is None or tags is None:
        return jsonify({'success': False})

    new_listing = Listing(None, title, tags, desc, price, bin(int(images, 2)), uid)
    db.session.add(new_listing)

    try:
        db.session.commit()
    except DatabaseError or DataError or IntegrityError:
        db.session.rollback()
        db.session.flush()
        return jsonify({'success': False})

    return jsonify({'success': True})


if __name__ == '__main__':
    db_init(app)
    app.run(host='localhost', port=5050)
