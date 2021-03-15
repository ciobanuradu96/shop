from flask import Blueprint, render_template, request, url_for, flash, redirect, jsonify
from flask.globals import session
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

@views.route('/cart', methods=['POST','GET'])
def cart():
    return render_template('cart.html',cart_item=cart_item)

@views.route('/add-to-cart',methods=['POST'])
def add_to_cart():
    product = json.loads(request.data)
    productId = product['productId']
    cart_item = Product.query.filter_by(id=productId).first()
    
    
    return cart_item    

