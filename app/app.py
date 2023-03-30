from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
from flask import request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from form import ListForm, FilterForm
from sqlalchemy import text



app = Flask(__name__)
#database with sqlachemy
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///owners.db'
#key for form
with open("app/key.json","r") as KEY:
    app.config['SECRET_KEY']= json.load(KEY)
app.app_context().push()  #validate hora db ki entries

db = SQLAlchemy(app)
session = db.session() 
app.app_context().push()  #validate hora db ki entries

class Owners(db.Model):
    list_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(150), nullable = False, unique=True)
    pricing = db.Column(db.Integer,nullable=False)
    location = db.Column(db.String(200),nullable=False)
    carpet_size= db.Column(db.Integer,nullable=False)
    contact = db.Column(db.Integer,unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)
    image_filename = db.Column(db.String)
    image_url = db.Column(db.String)

    #string creation
    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/')

def index():

    return render_template("index.html")

@app.errorhandler(404)

def page_not_found(e):

    return render_template('404.html')

@app.route('/list',methods=['GET','POST'])

def list():
    
    name=None
    form = ListForm()
    # validate the form
    if form.validate_on_submit():
            user=Owners(name=form.name.data,
            email=form.email.data,
            pricing=form.pricing.data,
            location=form.location.data,
            carpet_size=form.carpet_size.data,
            contact=form.contact.data,
            image_filename=form.photo.data)

            db.session.add(user)
            db.session.commit()
            
            name = form.name.data
            
            form.name.data=''
            form.email.data=''
            form.location.data=''
            form.carpet_size.data=''
            form.contact.data=''
            form.photo.data=''
    return render_template("list.html",form=form,name=name)

@app.route('/rent',methods=['GET','POST'])

def rent():
    
    form = FilterForm()
    
    if form.validate_on_submit():
        lower_range=form.least_price.data
        upper_range=form.asking_price.data
        price = {"minimum": lower_range, "maximum": upper_range}
        location=form.location.data
        carpet_size=form.carpet_size.data
        data={"pricing": price, "location": location, "carpet_size": carpet_size}

        query = text("SELECT pricing ,carpet_size ,location \
                    FROM owners  \
                    WHERE location='{}'AND\
                    pricing BETWEEN {} AND {} AND\
                    carpet_size='{}'".format(location,lower_range,upper_range,carpet_size))
        # execute query and fetch all results
        cursor = session.execute(query).cursor
        result = cursor.fetchall()
        
        return render_template("search.html",data=data, cursor=cursor,result=result)
        
    return render_template("rent.html",form=form)