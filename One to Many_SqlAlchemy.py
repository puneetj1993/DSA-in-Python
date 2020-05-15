from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

#one to many relationship (Person can have multiple pets but pet can have only single owner)
class Person(db.Model):

    ids = db.Column(db.Integer, primary_key = True)
    name = db.Column( db.String(80))
    #Created a back reference 'Owner' using backref and stores it in pets object
    pets = db.relationship('Pet',backref = 'owner')

    
class Pet(db.Model):
    ids = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    #Owner_id is a column depicting Foreign key
    owner_id = db.Column(db.Integer, db.ForeignKey('person.ids'))


#Shell statement
    
res = Person.query.filter_by(ids=1).first() #res object has result of this satement
# Simple things which are directly applicable as there are part of Person table itself
res.ids >> 1
res.name >> Puneet
#We are trying to access pets column on res. It gives a result in the list since this is one to many(Person can have multiple pets).
res.pets >> [pet<2>]
#If we want to acess Pet table columns , we can do using pets[i] since pets is a list and then column name in Pet table
res.pets[0].name
res.pets[0].ids
res.pets[0].owner_id

# Similarly, We can use the relation on Pet table
res1 = Pet.query.filter_by(name="Stella").first()
# Pet columns can be directly applied
res1.ids
res1.name
res1.owner_id

#Now, we will access Person table columns using owner backref
res1.owner.name          >> Puneet
res1.owner.ids           >>1
res1.owner.pets[0].name  >>stella

#In this way we can use owner backref on Person table and pets column on Pet table

if __name__ == "__main__":
    app.run(debug=True)
