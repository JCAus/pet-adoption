from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_PET_IMG = 'https://www.pngkey.com/png/detail/56-560960_dog-and-cat-drawing-at-getdrawings-cat-and.png'

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                    primary_key=True)

    name = db.Column(db.String(25), unique=True, nullable=False)

    species = db.Column(db.String(25), nullable=False)

    photo_url = db.Column(db.String(400), default=DEFAULT_PET_IMG)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.String(500), nullable=True)

    available = db.Column(db.String(5), nullable=False, default=True)