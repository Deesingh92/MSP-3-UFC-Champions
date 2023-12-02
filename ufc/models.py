from datetime import datetime
from ufc import db


class WeightClass(db.Model):
    # Schema for the WeightClass model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    champions = db.relationship("Champion", backref="weight_class", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Champion(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    weight_class_id = db.Column(db.Integer, db.ForeignKey("weight_class.id", ondelete="CASCADE"), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Champion: {1} | Weight Class: {2}".format(
            self.id, self.name, self.weight_class.name
        )
