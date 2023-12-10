import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ufc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from ufc import routes  # noqa