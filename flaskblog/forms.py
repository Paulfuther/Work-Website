from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FormField, DateField, SelectField
from wtforms.fields.html5 import DateField
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
    firstname = StringField('Firstname') ##, validators= [DataRequired(), Length(min=2, max=20)])
    nickname = StringField('Nickname')#, vlaidators= [Optional(), Length(max=20)])
    lastname = StringField('Lastname')#, validators = [DataRequired(), Length(min=2, max=20) ])
    store = SelectField('Store' , choices = [('Home Store', 'Home Store'),("396", "396"),('398','398'),
                                             ('402','402'),('414','414'),('1616','1616'),('8156','8156'),
                                             ('8435','8435'),('33410','33410'),
                                             ('33485','33485'),('48314', '48314'),
                                             ('65077','65077'),('65231','65231')])
    addressone = StringField('Address Line 1')
    addresstwo = StringField('Address Line 2')
    apt = StringField('Unit/Apt')
    city = StringField('City')
    province = StringField('Province')
    country = StringField('Country')
    email = StringField('Email')#, validators = [DataRequired(), Email()])
    mobilephone = StringField('mobile')#, vlidators = [DataRequired(), Length(min=9, max= 12)])
    sin = StringField('sin')# , validators = [DataRequired(), Length(min=9, max=9)])
    startdate = DateField('Start Date', format = '%y-%m-%d')                       
    enddate = DateField('End Date', format='%y-%m-%d')
    
    
    
    
    

