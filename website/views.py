from flask import Blueprint, render_template, request, url_for, flash
from . import db
from .models import Product
views = Blueprint('views', __name__)


@views.route('/', methods=["GET"])
def home():
    return render_template("index.html")


@views.route('/shop', methods=["GET", "POST"])
def shop():
    return render_template("products.html")


@views.route('/admin', methods=["GET", "POST"])
def admin_panel():
    if request.method == 'POST':
        product_name = request.form.get('productName')
        product_price = request.form.get('productPrice')
        product_image = request.form.get('imageLink')

        product_name = Product.query.filter_by(name=product_name)
        if product_name:
            flash('Product already exists', category='error')
        else:
            product = Product(name=product_name,
                              price=product_price, image=product_image)
            db.session.add(product)
            db.session.comit()
            flash('Product added!', category='success')
            return redirect(url_for('views.admin_panel'))
    return render_template("admin.html")
