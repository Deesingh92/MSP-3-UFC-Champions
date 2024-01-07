import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

if os.path.exists("env.py"):
    import env  # noqa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pmecelvg:5cFMdsgnnSgXPuNsE81qQzVl84T0hnLd@surus.db.elephantsql.com/pmecelvg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 40
app.config['SECRET_KEY'] = 'your_secret_key_here'

if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from ufc.models import User 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from ufc import routes  # noqa
