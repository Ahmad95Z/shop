import os
from werkzeug.utils import secure_filename
from shops import app
from flask import render_template, request
from shops.models import Product, db
from PIL import Image


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template ('index.html')

@app.route('/shop')
def shop():
    products=Product.query.all()
    return render_template ('shop.html', products=products)

@app.route('/product')
def product():
    return render_template ('product-details.html')

@app.route('/cart')
def cart():
    return render_template ('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == "POST":
        f=request.form
        image= request.files.get('image')
        if image:
            file_name=image.filename
            image=Image.open(image)
            image.save('shops/static/img/product-img/'+ file_name)
        p= Product(title=f.get('title'),price=f.get('price'),category=f.get('category'),availibility=f.get('availibility'),description=f.get('description'),image=file_name)
        db.session.add(p)
        db.session.commit()
    return render_template('add_product.html')