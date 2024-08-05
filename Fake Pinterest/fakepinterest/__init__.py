from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
database = SQLAlchemy(app)
app.config["SECRET_KEY"] = "e6e7b0fbaabqqdd98362b3c12db4040d97"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = 'homepage'

from fakepinterest.models import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

from fakepinterest import routes