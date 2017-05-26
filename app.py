from flask import Flask
app = Flask(__name__)
import views
from flask_login import LoginManager, current_user
from flask import Flask
from flask import session
from models import User
from models import Session
import datetime
from peewee import *



print("User >> ", User.table_exists())
if not User.table_exists():
    User.create_table()

print("Session >> ", User.table_exists())
if not Session.table_exists():
    Session.create_table()




app.debug = False
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.permanent_session_lifetime = datetime.timedelta(1000)
# Инициализируем его и задаем действие "входа"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
