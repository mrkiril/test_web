from app import app
from models import *
from flask import render_template
from flask import Flask
from flask import request
from flask import send_from_directory
from flask import session
from flask import redirect
from flask import escape
from flask import url_for
from flask_login import LoginManager, current_user
from flask_login import login_user, logout_user, login_required
from session_mode import *
import datetime
from models import Session
import json

@app.route('/')
def redir():
    return redirect(url_for('main'))

@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    dick = {
            "domen": url_for('reg'),
            "error": False
            }
    if request.method == "GET":
        return render_template("registration.html", posts=dick)
    try:
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
    except Exception as e:
        return redirect(url_for('logout'))
   
    try:        
        new_user = User.create(
            username=username,
            password=User.hash_password(password1),
            salt='salt')
    except Exception as e:
        dick['error'] = "Try another username"
        return render_template("registration.html",
                               posts=dick)
    if password1 != password2:
        dick['error'] = 'Input incorrect data. pass1 not equal pass2.'
        return redirect(url_for('reg'))

    session['twit'] = add_new_ses(new_user)
    return redirect(url_for('main'))


@app.route('/auth/', methods=['GET', 'POST'])
def auth():
    dick = {
            "domen": url_for('auth'),
            "reg_page": url_for('reg'),
            'username': True
    }

    if session.get('twit'):
        if is_active_ses(session['twit']):
            return redirect(url_for('main'))
        return redirect(url_for('auth'))

    if request.method == "POST":
        try:
            username = request.form["enter_email"]
            password = request.form["password"]
        except KeyError as e:
            return redirect(url_for('logout'))
        
        user = User.is_user_in_db(
            user=username,
            password=password)
        if user:
            session['twit'] = add_new_ses(user)
            return redirect(url_for('main'))
        dick['username'] = False
    return render_template("authorisation.html",
                           posts=dick)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if 'twit' not in session:
        return redirect(url_for('auth'))
    pop_session(session['twit'])
    session.pop('twit', None)    
    return redirect(url_for('auth'))


@app.route('/main/')
def main(): 
    cur_user = auth_foo(session)
    if type(cur_user) is not Session:
        return cur_user
    
    blog_dick = {
        'user': cur_user.ses_user.username,
        'delete_user': '/main/del/',        
        'add_user_link': url_for('user_add'),
        'logout': url_for('logout'),             
    }    
    blog_dick['users'] = User.select()
    return render_template("forms.html",
                           posts=blog_dick)


@app.route('/main/add/', methods=['POST'])
def user_add():
    dick = {}
    cur_user = auth_foo(session)
    if type(cur_user) is not Session:
        return cur_user

    username = request.form["add_username"]
    password = request.form["add_password"]
    try:        
        new_user = User.create(
            username=username,
            password=User.hash_password(password),
            salt='salt')
    except Exception as e:
        if password == "":
            dick['error'] = "Password is empty"
        else:
            dick['error'] = "Try enother username"
        return json.dumps(dick)

    return json.dumps({'USERNAME' : new_user.username, "ID": new_user.id})
    
@app.route('/main/del/', methods=['POST'])
def user_del():
    dick = {}
    cur_user = auth_foo(session)    
    if type(cur_user) is not Session:
        return cur_user


    num = request.form["del"]
    try:
        user = User.get(User.id == num)
        user.delete_instance()            
        
    except Exception as e:
        dick['error'] = "Sorry. You must have the rights of the admin"
        return json.dumps(dick)

    return json.dumps({"ID": num})

def auth_foo(ses):
    try:
        cur_user = is_active_ses(ses['twit'])
        if not cur_user:
            return redirect(url_for('logout'))
    except KeyError as e:
        return redirect(url_for('logout'))
    else:
        return cur_user