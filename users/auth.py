from flask import Blueprint,render_template

user_auth = Blueprint('user_auth',__name__,template_folder="templates")

@user_auth.route('/',methods=['POST','GET'])
def login():
    return render_template('login.html')
