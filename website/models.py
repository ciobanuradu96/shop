from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    price = db.Column(db.Integer)
    image = db.Column(db.String(1000))
