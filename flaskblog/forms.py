from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FormField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flaskblog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign-Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That Username is Taken. Please choose a different one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That Email is Taken. Please choose a different one')      


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                'That Username is Taken. Please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                'That Email is Taken. Please choose a different one')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
    
    
class EmployeeForm(FlaskForm):
    firstname = StringField('firstname') ##, validators= [DataRequired(), Length(min=2, max=20)])
    nickname = StringField('nickname')#, vlaidators= [Optional(), Length(max=20)])
    lastname = StringField('lastname')#, validators = [DataRequired(), Length(min=2, max=20) ])
    email = StringField('email')#, validators = [DataRequired(), Email()])
    mobilephone = StringField('mobile')#, vlidators = [DataRequired(), Length(min=9, max= 12)])
    sin = StringField('sin')# , validators = [DataRequired(), Length(min=9, max=9)])
    startdate = FormField(DateField)                        
    enddate = FormField(DateField)
    
    
    
    
    

