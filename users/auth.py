from flask import Blueprint,render_template

user_auth = Blueprint('user_auth',__name__,template_folder="templates")

#login route
@user_auth.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')

#signup route
@user_auth.route('/signup',methods=['POST','GET'])
def signup():
    return render_template('signup.html')
