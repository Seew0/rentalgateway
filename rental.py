from flask import Flask, jsonify, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,EmailField
from wtforms.validators import DataRequired
from flask_sqlalchemy import   SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask import request
import json

app = Flask(__name__)


#database with sqlachemy


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///owners.db'

#key for form
with open("hidden.json","r") as KEY:
    app.config['SECRET_KEY']= json.load(KEY)
#init db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Owners(db.Model):
    listing_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable = False, unique=True)
    pricing = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(200),nullable=False)
    contacts = db.Column(db.Integer,unique=True)
    carpet_size= db.Column(db.Integer,nullable=False)


        #STRING CREATE HORI
    def __repr__(self):
        return '<Name %r>' % self.name


class UserForm(FlaskForm):
    name= StringField("Name",validators=[DataRequired()])
    email= EmailField("Email",validators=[DataRequired()])
    pricing= IntegerField("Pricing",validators=[DataRequired()])
    location= StringField("Location",validators=[DataRequired()])
    contacts= IntegerField("Contact Number",validators=[DataRequired()])
    carpet_size= IntegerField("Carpet Size",validators=[DataRequired()])
    submit= SubmitField("Submit")


class FilterForm(FlaskForm):
    minimum_price= IntegerField("Minimum Price",validators=[DataRequired()])
    maximum_price= IntegerField("Maximum Price",validators=[DataRequired()])
    location= StringField("Location",validators=[DataRequired()])
    carpet_size= IntegerField("Carpet Size",validators=[DataRequired()])
    submit= SubmitField("Submit")

@app.route('/')

def index():
    return render_template("index.html")


@app.errorhandler(404)

def page_not_found(e):
    return render_template('404.html')

@app.route('/listing',methods=['GET','POST'])

def listing():
    form = UserForm()
    name=None
    if form.validate_on_submit():
        user=Owners(name=form.name.data,
        email=form.email.data,pricing=form.pricing.data,
        location=form.location.data,
        contacts=form.contacts.data,
        carpet_size=form.carpet_size.data
        )
        db.session.add(user)
        db.session.commit()
    name = form.name.data
    form.name.data=''
    form.email.data=''
    form.location.data=''
    form.contacts.data=''
    form.carpet_size.data=''
    flash("Listed Successfully!!")
    our_users=Owners.query.order_by(Owners.name)
    return render_template("listing.html",form=form,
    name=name,our_users=our_users)

@app.route('/filter',methods=['GET','POST'])

def filter():
    form = FilterForm()
    if form.validate_on_submit():
        minimum_price=form.minimum_price.data
        maximum_price=form.maximum_price.data
        price = {"minimum": minimum_price, "maximum": maximum_price}
        location=form.location.data
        carpet_size=form.carpet_size.data
        data={"pricing": price, "location": location, "carpet_size": carpet_size}
        query = "select * from owners where true"
        if data['location'] != "":
            query += " and location = '{}'".format(data['location'])
        if data['carpet_size'] != "":
            query += " and carpet_size = {}".format(data['carpet_size'])
        if data['pricing'] != "":
            minimum = data['pricing']["minimum"]
            maximum = data['pricing']["maximum"]
            query += " and pricing between {} and {}".format(minimum, maximum)
    
    # execute query and fetch all results
        results = db.engine.execute(query)
        return render_template("search.html",data=data) 
        

    return render_template("filter.html",form=form)



