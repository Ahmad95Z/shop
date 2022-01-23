from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from config import *

app= Flask(__name__)
db= SQLAlchemy (app)
app.config.from_object(Config)
migrate= Migrate (app, db)


from shops import routes, models