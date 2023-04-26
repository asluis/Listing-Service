from flask import Flask, Response
from flask import request
from sqlalchemy.exc import DatabaseError, DataError, IntegrityError
from models.Listing import Listing
from models.Images import Images
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
@app.route('/api/v1/create/<uid>/<title>/<price>/<desc>/<tags>', methods=['POST'])
def create_listing(uid: str = None, title: str = None, price: float = 0.00, desc: str = "",
                   tags: str = None) -> Response:
    if uid is None or title is None or price is None or desc is None or tags is None:
        return jsonify({'success': False})

    new_listing = Listing(None, title, tags, desc, price, uid)
    db.session.add(new_listing)

    try:
        db.session.commit()
    except DatabaseError or DataError or IntegrityError:
        db.session.rollback()
        db.session.flush()
        return jsonify({'success': False})

    return jsonify({'success': True})


"""
POST: /api/v1/images/?imgs=[]&listing_id=INT
* Requires
    - imgs: a list of images (files)
    - listing_id: corresponding listing id
WARNING: This has not been fully tested. TODO: test
"""
@app.route('/api/v1/images/', methods=['POST'])
def postImages() -> Response:
    listing_id = request.args.get('listing_id')
    imgs = request.files.getlist('imgs')

    if listing_id is None or imgs is None:
        return jsonify({'success': False})

    # Add each image to db and commit
    for i in range(len(imgs)):
        app.logger.info(f'TEST: {imgs[i]}')
        image_mimetype = image_data.mimetype
        image_data = imgs[i].read()  # Gets data for ith image

        new_image = Images(None, listing_id, image_data, image_mimetype)  # Creates image DB object
        db.session.add(new_image)

        # Commit images to database—does so for every image to prevent diff. API calls overriding the same image ID
        try:
            db.session.commit()
        except DatabaseError or DataError or IntegrityError:
            db.session.rollback()
            db.session.flush()
            return jsonify({'success': False})

    return jsonify({'success': True})


"""
See here for passing a list of images using request.files.getlist: 
https://stackoverflow.com/questions/70754829/upload-files-and-a-string-in-same-flask-request

GET: /api/v1/images/<listing_id>
* Gets all images associated with a listing_id 
* Returns: 
    - success status
    - data (dict) consisting of 
        - count: index of list of images
        - img: image data
        - mimetype: type of image (jpg vs jpeg vs png vs ...)
        - listing_id: listing_id this image belongs to
    - data_length: number of images returned
"""
@app.route('/api/v1/images/<listing_id>', methods=['GET'])
def getImages(listing_id: int = None) -> Response:

    if listing_id is None:
        return jsonify({'success': True})

    images_query = []

    try:
        images_query = db.session.query(Images).filter(Images.listing_id == listing_id).all()
    except DatabaseError or DataError or IntegrityError:
        db.session.rollback()
        db.session.flush()
        return jsonify({'success': False})

    data: [dict] = []
    # Iterate thru all images fetched from DB and add each image's data into a dict, which is then added to a list
    for i in range(len(images_query)):
        curr_image = images_query[i]
        curr_data = {
            'count': i,
            'img': curr_image.data,
            'mimetype': curr_image.mimetype,
            'listing_id': curr_data.listing_id
        }

        data.append(curr_data)

    return jsonify({
        'success': True,
        'data': data,
        'data_length': len(data)
    })


if __name__ == '__main__':
    db_init(app)
    app.run(host='localhost', port=5050, debug=True)
