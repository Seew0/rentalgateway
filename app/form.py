from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class ListForm(FlaskForm):
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
    photo = FileField(
        "photo", validators=[FileRequired() ,FileAllowed(['jpg','jpeg','png']),'Images only!']
        )
    submit= SubmitField("Submit")


class FilterForm(FlaskForm):
    least_price= IntegerField(
        "Lower Range",validators=[DataRequired()]
        )
    asking_price= IntegerField(
        "Upper Range",validators=[DataRequired()]
        )
    location= StringField(
        "Location",validators=[DataRequired()]
        )
    contact= IntegerField(
        "What is Your Contact Number",validators=[DataRequired()]
        )
    carpet_size= IntegerField(
        "Carpet Size",validators=[DataRequired()]
        )
    submit= SubmitField("Submit")