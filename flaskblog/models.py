from flaskblog import db, login_manager
from flaskblog import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Employee(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=True)
    nickname = db.Column(db.String(20), unique = False, nullable=True)
    Lastname = db.Column(db.String(20), unique = True, nullable=True)
    store = db.Column(db.Integer, unique = False, nullable=True)
    addressone = db.Column(db.String(20))
    addresstwo = db.Column(db.String(20))
    apt = db.Column(db.String(20))
    city = db.Column(db.String(20))
    province = db.Column(db.String(20))
    country = db.Column(db.String(20))
    mobilephone= db.Column(db.String(10), unique = True, nullable=True)
    email=db.Column(db.String(120), unique=True, nullable=True)
    SIN = db.Column(db.Integer, unique=True, nullable=True)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    Startdate = db.Column(db.DateTime())
    Enddate = db.Column(db.DateTime())
   
    
    def __repr__(self):
        return f"Employee('{self.firstname}', '{self.SIN}')"
