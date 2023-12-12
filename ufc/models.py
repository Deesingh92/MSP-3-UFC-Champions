from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Champion(db.Model):
    __tablename__ = 'champions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String, nullable=False)
    weight_class = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    image_url = db.Column(db.String)

    def __init__(self, name, country, weight_class, start_date, end_date=None, image_url=None):
        self.name = name
        self.country = country
        self.weight_class = weight_class
        self.start_date = start_date
        self.end_date = end_date
        self.image_url = image_url

    def __repr__(self):
        return f"<Champion {self.name}>"

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
    def get_id(self):
        return str(self.id)
