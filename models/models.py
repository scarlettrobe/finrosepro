from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # use sqlite database file named app.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), index=True)
    information = db.Column(db.String(120))

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float)
    rent = db.Column(db.Float)
    utilities = db.Column(db.Float)
    groceries = db.Column(db.Float)
    others = db.Column(db.Float)
    plan = db.Column(db.String(120))

class Spending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.Float)
    entertainment = db.Column(db.Float)
    transportation = db.Column(db.Float)
    others = db.Column(db.Float)
    analysis = db.Column(db.String(120))
