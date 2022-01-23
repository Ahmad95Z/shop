from posixpath import realpath
from flask import app, config
from os.path import join, dirname, realpath




class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shops.db'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
