from email import message
from utils.db import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80), nullable = True)
    lastname = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    
    def __init__(self, firstname, lastname, email, message):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.message = message
