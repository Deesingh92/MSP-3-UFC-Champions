from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Champion(db.Model):
    __tablename__ = 'champions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    country = db.Column(db.String)
    weight_class = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    image_url = db.Column(db.String)

    def __init__(self, name, country, weight_class, start_date, end_date, image_url):
        self.name = name
        self.country = country
        self.weight_class = weight_class
        self.start_date = start_date
        self.end_date = end_date
        self.image_url = image_url

    def __repr__(self):
        return f"<Champion {self.name}>"
