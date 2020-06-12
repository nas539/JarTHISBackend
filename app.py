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



class AdminClass:
    def admin_del (username) :
        user_to_del = username
        for (attribute in user):
            del attribute
            print("Username was deleted.")

    def admin_del_recipe(recipe) :
        recipe_to_del = recipe
        del recipe_to_del
        print ("Recipe was deleted")  
    


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



<<<<<<< HEAD
class Recipe():
    def __init__(self, name, ID, AddedBy, Tag ):
        self.name = name
        self.ID = ID
        self.AddedBy = AddedBy
        self.Tag

=======
>>>>>>> 96a38fa8cf997d6341a23b46c7cf340838980c52

if __name__ == "__main__":
    app.debug = True
    app.run()


