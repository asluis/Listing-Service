"""
This file is here to prevent circular import errors. Place all flask-sqlalchemy database related instances
here if you need to access them from separate files.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creates all tables
def db_init(app) -> None:
    with app.app_context():
        db.init_app(app)
        db.create_all()
