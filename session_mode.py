from models import Session
from models import User
import datetime
import random
import string

def add_new_ses(user):
    while True:
        ses_id = ''.join([random.choice(string.hexdigits) for i in range(16)])
        delta = datetime.timedelta(seconds=1000)
        dt = datetime.datetime.utcnow()
        try:
            Session.create(
                token=ses_id, 
                ses_user=user, 
                expires=dt+delta)
        except Exception as e:
            print(e)
            continue
        else:
            return ses_id
    

def pop_session(token):
    try:
        ses = Session.get(token=token)
        ses.delete_instance()  
    except Exception as e:
        print(e)        
    else:
        return True


def is_active_ses(token):
    try:
        ses = Session.get(token=token)        
    except Exception as e:
        print(e)
        raise e
    else:
        if ses:
            return ses
        else:
            return False





































