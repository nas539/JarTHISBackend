from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ""

db = SQLAlchemy(app)
ma = Marshmallow(app)
heroku = Heroku(app)
CORS(app)



class Recipe(db.model):
    Name = db.Column(db.String(), primary_key=True)
    ID = db.Column(db.Integer, nullable = False
    AddedBy = db.Column(db.String(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullabe=False)
    email = db.Column(db.String, nullable=True )
    isAdmin = db.Column(db.Boolean)
    isLoggedIn = db.Column(db.Boolean)
    bio = db.Column(db.String)



class Recipe():
    def __init__(self, name, ID, AddedBy, Tag ):
        self.name = name
        self.ID = ID
        self.AddedBy = AddedBy
        self.Tag


if __name__ == "__main__":
    app.debug = True
    app.run()


