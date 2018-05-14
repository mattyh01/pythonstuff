#Forms using flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Import password generator.py?

class RegistrationForm(FlaskForm): #Inherit from flask template
    username = StringField('username',
               validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
            validators=[DataRequired(), Email()])
    password = PasswordField('password',
               validators=[DataRequired()])
    password_confirm = PasswordField('confirm password',
                       validators=[DataRequired(), equalto('password')])
    submit = SubmitField('Sign up')
