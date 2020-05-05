from .import db

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
    
   


