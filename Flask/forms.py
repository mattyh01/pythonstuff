#Forms using flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Import password generator.py
#Secret key - will protect against cross site attacks, modifying cookies,
#forgery etc

class RegistrationForm(FlaskForm): #Inherit from flask template
    username = StringField('Username',
               validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail',
            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
               validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password',
                       validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm): #Inherit from flask template
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
               validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
