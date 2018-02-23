from flask import Flask

app = Flask(__name__)

#import stuff
from users.auth import user_auth

#register blueprints
app.register_blueprint(auth.user_auth)
