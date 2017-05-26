from peewee import *
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import LoginManager
import datetime


mysql_db = MySQLDatabase('myproject', 
    user="myprojectuser",
    password='password' )

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mysql_db

class User(BaseModel):    
    username = CharField(null=False, unique=True)
    password = BlobField(null=False)
    salt = BlobField(null=False)
    
    def is_authenticated():
        return True

    def is_active():
        return True

    def is_anonymous():
        return False

    def get_id(self):
        return str(self.id)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password).decode('utf-8')

    @staticmethod
    def is_user_in_db(user, password):
        try:            
            try_user = User.get(
                User.username == user)
         
        except Exception as e:
            return None
        else:
            if try_user.check_password(password):
                return try_user
            else:
                return None 

class Session(BaseModel):
    token = CharField(null=False, primary_key=True)
    ses_user = ForeignKeyField(User, related_name='ses_user')    
    expires = DateTimeField(default=datetime.datetime.now)





