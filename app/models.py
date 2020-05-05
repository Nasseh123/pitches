from .import db
from werkzeug.security import generate_password_hash,check_password_hash
class Pitch:
    """
    category objects to define category objects
    """
    def __init__(self,id,pitch,author):
        self.id=id
        self.pitch=pitch
        self.author=author

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    # pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))
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


    def __repr__(self):
            return f'User {self.username}'

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'
# class Pitches(db.Model):
#     __tablename__='pitch'

#     id=db.Column(db.Integer,primary_key=True)
#     # pitch=db.relationship('User',backref='pitch',lazy='dynamic')
#     def __repr__(self):
#         return f'User {self.pitch}'
    
   


