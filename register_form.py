from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length, EqualTo, ValidationError
from models import *
from passlib.hash import pbkdf2_sha256

def invalid_credentials(form,field):
    username_entered = form.username.data
    password_entered = field.data

    user_obj = User.query.filter_by(username=username_entered).first()
    if user_obj is None:
        raise ValidationError("No Account Found")
    elif not pbkdf2_sha256.verify(password_entered,user_obj.password):
        raise ValidationError("Username or password incorrect!!")




class Registration_form(FlaskForm):
    firstname = StringField('firstname-label',
        validators=[InputRequired(message="Name cannot be empty!")])

    lastname = StringField('lastname-label',
        validators=[InputRequired(message="Name cannot be empty!")])

    username = StringField('username-label',
        validators=[InputRequired(message="Username cannot be Empty"),
        Length(min=4,max=10,message="length greater than 4")])

    password = PasswordField('password-field',
        validators=[InputRequired(message="Password Required")])

    retype_pwd = PasswordField('password-field',
        validators=[InputRequired(message="Password Required"),
        EqualTo('password', message="Password Does not match")])

    contactno  = StringField('contact-label',
        validators=[InputRequired(message="Contact is Required"),
        Length(min=10,max=10,message="Invalid contact")])

    submit_button = SubmitField('Create Account')

    def validate_username(self,username):
        #username = username.data
        user_obj = User.query.filter_by(username=username.data).first()
        if user_obj:
            raise ValidationError("Username Already taken!!")



class Login_form(FlaskForm):
    username = StringField('username-label',
        validators=[InputRequired(message="Username Required")])

    password = PasswordField('password-label',
        validators=[InputRequired(message="Password Required"),
            invalid_credentials])

    submit_button = SubmitField('Login')