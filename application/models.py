from flask_sqlalchemy import SQLAlchemy
from flask_security.core import UserMixin,RoleMixin

db=SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement = True, primary_key=True)
    email = db.Column(db.String, unique=True)
    username=db.Column(db.String, unique=False)
    password = db.Column(db.String(20))
    active = db.Column(db.Boolean()) 
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)  
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    roles = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy='dynamic'))

class User_Role(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column('user_id',db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column('role_id',db.Integer,db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True,autoincrement= True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(300))

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key = True, autoincrement=True)
    name = db.Column(db.String,unique = True, nullable = False)
    description = db.Column(db.String,nullable = False)
    active = db.Column(db.Boolean())
    
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False,unique = True)
    description = db.Column(db.String, nullable=False)
    section = db.Column(db.String, db.ForeignKey('category.name'))
    quantity = db.Column(db.Integer,nullable = False)
    amount = db.Column(db.Integer,nullable = False)
    

