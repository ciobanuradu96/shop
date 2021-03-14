from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000), unique=True)
    price = db.Column(db.Float)
    image = db.Column(db.String(10000))
