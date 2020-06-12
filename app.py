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
# he


class Recipe(db.model):
    Name = db.Column(db.String(), primary_key=True)
    ID = db.Column(db.Integer, nullable = False
    AddedBy = db.Column(db.String(), nullable=False)


class Recipe():
    def __init__(self, name, ID, AddedBy, Tag ):
        self.name = name
        self.ID = ID
        self.AddedBy = AddedBy
        self.Tag


class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email', 'isAdmin', 'isLoggedIn', 'bio')

users_schema = UserSchema(many=True)



if __name__ == "__main__":
    app.debug = True
    app.run()


