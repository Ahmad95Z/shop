# from crypt import methods
import email
import imp
import os
from click import password_option
from werkzeug.utils import secure_filename
from shops import app
from flask import render_template, request, redirect, url_for, flash
from shops import forms
from shops.models import Product, db , User,Buy
from PIL import Image
from flask_login import login_user, logout_user, current_user
from shops.forms import RegistrationForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template ('index.html')


@app.route('/shop')
def shop():
    products=Product.query.all()
    return render_template ('shop.html',products=products)

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
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect (url_for('index'))
    if request.method== 'POST':
        user=User.query.filter_by(email=request.form.get('email')).first()
        if user and user.password == request.form.get('password'):
            login_user(user)
        return render_template ('index.html')
    return render_template('login.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
        logout_user()
        return redirect(url_for('index'))

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product-details.html', product=product)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('???????????????????????? ???????????? ??????????????!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)

@app.route('/products/<int:product_id>/buy', methods=['GET', 'POST'])
def buy(product_id):
    product = Product.query.get(product_id)
    if request.method == "POST":
        f = request.form
        b = Buy(name=f.get('name'), adress=f.get('adress'), email=f.get(
            'email'), product=product)
        db.session.add(b)
        db.session.commit()
        return redirect ('/buys')
    return render_template('buy.html')


@app.route('/buys')
def buys():
    buys = Buy.query.all()
    return render_template('buys.html', buys=buys)


@app.route('/shops/<int:product_id>/del/')
def product_delete(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return redirect ('/shop')
