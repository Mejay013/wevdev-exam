from flask_login import UserMixin
from datetime import datetime
from .app import db 

class Appeal(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type_appeal = db.Column(db.Integer, db.ForeignKey('appeal_type.id'), nullable=False)
    status_appeal = db.Column(db.Integer, db.ForeignKey('appeal_status.id'), nullable=False)
    message_appeal = db.Column(db.Text, nullable=False)

class Appeal_type(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_appeal = db.Column(db.String(255) , nullable=False)

class Appeal_status(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_appeal = db.Column(db.String(255), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    user_fio = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

class Role(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text, nullable=False)