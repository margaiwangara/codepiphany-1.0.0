from flask import Flask,request,session,abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__,instance_relative_config=True)

#define csrf token
@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = os.urandom(24)
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

#connect SQLAlchemy
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

#import stuff
from users.auth import user_auth

#register blueprints
app.register_blueprint(auth.user_auth)
