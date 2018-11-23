from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class DetailsForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Age = IntegerField("Age")
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   
   submit = SubmitField("Send")
