from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db=SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = "info"
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(30),nullable=False)
    lastname = db.Column(db.String(30),nullable=False)
    username = db.Column(db.String(25),unique=True,nullable=False)
    contactno = db.Column(db.String(15),nullable=False)
    password = db.Column(db.String(),nullable=False) 



