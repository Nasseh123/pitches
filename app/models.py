from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# class Pitch:
#     """
#     category objects to define category objects
#     """
#     def __init__(self,id,pitch,author):
#         self.id=id
#         self.pitch=pitch
#         self.author=author

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email =db.Column(db.String(255),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch=db.relationship('Pitch',backref='pitch',lazy='dynamic')
    pass_secure = db.Column(db.String(255))

# generate a password hash and pass the hashed password as a value to the pass_secure column property to save to the database.
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
       return check_password_hash(self.pass_secure,password)

    @classmethod
    def get_user(cls,id):
        user= User.query.filter_by(id=id).first()
        return user

    def __repr__(self):
            return f'User {self.username}'

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__='pitch'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    category=db.Column(db.String)
    description=db.Column(db.String)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    def __repr__(self):
        return f'User {self.pitch}'

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitch(cls,id):
        pitch= Pitch.query.filter_by(id=id).all()
        return pitch
# ******88RETURNS ALL PITCHES
    def get_all_pitch():
        pitch= Pitch.query.all()
        return pitch



    
   


