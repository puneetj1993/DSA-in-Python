from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

#Many to many relationship (Page can have multiple tags and vice versa). For Many to Many relationship, we will need a helper table(tags) 

class Page(db.Model):

    ids = db.Column(db.Integer, primary_key = True)
    #Created a back reference 'Owner' using backref and stores it in pets object
    tags = db.relationship('Tag',secondary = tags, backref = db.backref("pages",lazy=True))

    
class Tag(db.Model):
    ids = db.Column(db.Integer,primary_key=True)


#tags is a helper table with 2 columns both acts as a foreign key for Page and Tag table
tags = db.Table('tags',
        db.Column('tag_id' ,db.Integer, db.ForeignKey('tag.ids'),primar_key = True)
        db.Column('page_id' ,db.Integer, db.ForeignKey('page.ids'),primar_key = True))



#Shell statement
    


if __name__ == "__main__":
    app.run(debug=True)
