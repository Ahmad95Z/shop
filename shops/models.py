from multiprocessing.spawn import import_main_path
from flask_login import UserMixin
from sqlalchemy import false, true
from shops import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Product(db.Model):
    __tablename__= 'products'
    id= db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(), nullable=False)
    availibility = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(), nullable=False)
    buy = db.relationship('Buy', backref='product', lazy=True)

    def __repr__(self) -> str:
        return self.title

class User(db.Model,UserMixin):
    __tablename__='users'
    id= db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(),nullable=True, unique=true)
    password = db.Column(db.String(),nullable=True, unique=true)
    isAdmin = db.Column(db.Boolean(),default=False)
    def __repr__(self) -> str:
        return self.email

class Buy(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now)
    adress = db.Column(db.String(), nullable=False)
    product_id = db.Column(db.Integer(), db.ForeignKey(
        'products.id'))

    def __repr__(self) -> str:
        return self.email


