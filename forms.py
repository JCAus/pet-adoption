from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField 
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class Add_Pet_Form(FlaskForm):
    name = StringField('Name', validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField('Species', choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])

class Edit_Pet_Form(FlaskForm):
    
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])
    available = SelectField("Available?", choices=[("true", "Yes"), ("false", "No")])