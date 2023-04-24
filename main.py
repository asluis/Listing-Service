from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

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

db = SQLAlchemy(app)


@app.route('/api/v1/')
def main() -> dict:
    return {'response': '''This is University Pal's Listing microservice for everything related to a listing.'''}

# Creates all tables
def createTables() -> None:
    app.app_context().push()
    db.create_all()


if __name__ == '__main__':
    createTables()
    app.run(host='localhost', port=5050)
