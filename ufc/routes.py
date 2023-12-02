from flask import render_template
from ufc import app, db
from ufc.models import WeightClass, Champion


@app.route("/")
def home():
    return render_template("base.html")