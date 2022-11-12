from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, TextAreaField, FloatField
from wtforms.validators import DataRequired, EqualTo, NumberRange

class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   remember_me = BooleanField('Remember Me')
   submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   name = StringField("Display Name", validators=[DataRequired()])
   is_artist = BooleanField("I'm an artist")
   password = PasswordField('Password', validators=[DataRequired()])
   password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Register')

class PostForm(FlaskForm):
   image = FileField('Upload Image', validators=[DataRequired()])
   caption = TextAreaField('A Descriptive Caption', validators=[DataRequired()])
   price = FloatField('Price', validators=[NumberRange(min=0)])
   submit = SubmitField('Create')
