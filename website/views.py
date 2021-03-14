from flask import Blueprint, render_template, request, url_for, flash, redirect, jsonify
from . import db
from .models import Product
import simplejson as json
views = Blueprint('views', __name__)


@views.route('/', methods=["GET"])
def home():
    return render_template("index.html")


@views.route('/shop', methods=["GET", "POST"])
def shop():
    products = Product.query.all()
    return render_template("products.html", products=products)


@views.route('/admin', methods=["GET", "POST"])
def admin_panel():
    if request.method == 'POST':
        product_name = request.form.get('productName')
        product_price = request.form.get('productPrice')
        product_image = request.form.get('imageLink')
        product = Product(name=product_name,
                          price=product_price, image=product_image)
        db.session.add(product)
        db.session.commit()
        flash('Product added!', category='success')
    products = Product.query.all()
    return render_template("admin.html", products=products)


@views.route('/delete-product', methods=['POST'])
def delete_product():
    product = json.loads(request.data)
    productId = product['productId']
    product = Product.query.get(productId)
    if product:
        db.session.delete(product)
        db.session.commit()
    return Jsonify({})
