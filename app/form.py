from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

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
    submit= SubmitField("Submit")


class FilterForm(FlaskForm):
    least_price= IntegerField("Lower Range",validators=[DataRequired()])
    asking_price= IntegerField("Upper Range",validators=[DataRequired()])
    location= StringField("Location",validators=[DataRequired()])
    contact= IntegerField("What is Your Contact Number",validators=[DataRequired()])
    carpet_size= IntegerField("Carpet Size",validators=[DataRequired()])
    submit= SubmitField("Submit")