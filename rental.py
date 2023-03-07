from flask import Flask, jsonify, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from flask_sqlalchemy import   SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask import request
import json
from markupsafe import escape
from sqlalchemy import text

app = Flask(__name__)   #this is telling that this file is the main file


#database with sqlachemy
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///owners.db'

#key for form
with open("key.json","r") as KEY:
    app.config['SECRET_KEY']= json.load(KEY)

#init db
db = SQLAlchemy(app)

app.app_context().push()  #validate hora db ki entries

session = db.session()   #connectivity with db

class Owners(db.Model):
    listing_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable = False, unique=True)
    pricing = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(200),nullable=False)
    carpet_size= db.Column(db.Integer,nullable=False)
    contact = db.Column(db.Integer,unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)


    #string creation
    def __repr__(self):
        return '<Name %r>' % self.name


class UserForm(FlaskForm):
    name= StringField(
        "Name",validators=[DataRequired()]
        )
    email= EmailField(
        "Email",validators=[DataRequired()]
        )
    pricing= IntegerField(
        "Pricing",validators=[DataRequired()]
        )
    location= StringField(
        "Location",validators=[DataRequired()]
        )
    contact= IntegerField(
        "Contact Number",validators=[DataRequired()]
        )
    carpet_size= IntegerField(
        "Carpet Size",validators=[DataRequired()]
        )
    # photo = FileField(
    #     "photo", validators=[FileAllowed(['jpg','jpeg','png'])]
    #     )
    submit= SubmitField("Submit")


class FilterForm(FlaskForm):
    least_price= IntegerField("Lower Range",validators=[DataRequired()])
    asking_price= IntegerField("Upper Range",validators=[DataRequired()])
    location= StringField("Location",validators=[DataRequired()])
    contact= IntegerField("What is Your Contact Number",validators=[DataRequired()])
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
    name=None
    form = UserForm()
    # validate the form
    if form.validate_on_submit():
        user=Owners(name=form.name.data,
        email=form.email.data,
        pricing=form.pricing.data,
        location=form.location.data,
        carpet_size=form.carpet_size.data,
        contact=form.contact.data,
        # photo=form.photo.data
        )
        db.session.add(user)
        db.session.commit()
        name = form.name.data
        form.name.data=''
        form.email.data=''
        form.location.data=''
        form.carpet_size.data=''
        form.contact.data=''
        flash("Listed Successfully!!")
    our_users=Owners.query.order_by(Owners.data_added)
    return render_template("listing.html",form=form,
    name=name ,our_users=our_users)

@app.route('/filter',methods=['GET','POST'])

def filter():
    
    form = FilterForm()
    if form.validate_on_submit():
        lower_range=form.least_price.data
        upper_range=form.asking_price.data
        price = {"minimum": lower_range, "maximum": upper_range}
        location=form.location.data
        carpet_size=form.carpet_size.data
        data={"pricing": price, "location": location, "carpet_size": carpet_size}

        t = text("SELECT pricing ,carpet_size ,location \
                  FROM owners  \
                  WHERE location='{}'AND\
                        pricing BETWEEN {} AND {} AND\
                        carpet_size='{}'".format(location,lower_range,upper_range,carpet_size))
    # execute query and fetch all results
        cursor = session.execute(t).cursor
        result = cursor.fetchall()
        return render_template("search.html",data=data, cursor=cursor,result=result)
        

    return render_template("filter.html",form=form)
