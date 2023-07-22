from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
login_manager = LoginManager()
login_manager.login_view = "login"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# login manager ... 

from in_stock  import routes