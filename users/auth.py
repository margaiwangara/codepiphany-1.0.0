from flask import Blueprint,render_template,request,current_app
from instance.functions.functions import username_validation,password_match,validate_email
from passlib.hash import sha256_crypt
from instance.models.models import Users
from . import db

user_auth = Blueprint('user_auth',__name__,template_folder="templates")

#login route
@user_auth.route('/')
def index():
    return render_template('index.html')
    
@user_auth.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')
    if request.method == 'POST':
        #post method logger
        current_app.logger.info('Request method is POST')
        email = request.form['email']
        password = request.form['password']
        #return email and password
        return render_template('login.html',email=email,password=password)

#signup route
@user_auth.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        #log form submit
        current_app.logger.info('Post method initiated')
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        #pass user input through validation functions
        if username is not None:
            username = username_validation(username)
        if email is not None:
            email = validate_email(email)
        if password is not None:
            password = password_match(password,confirm_password)


        #check if output is not None
        if password is not None and email is not None and username is not None:
            #log success
            current_app.logger.info('Input validation passed')
            #encrypt password and print the result to the screen
            #encrypt password
            hashed_password = sha256_crypt.encrypt(str(password))

            #check user existance in db
            user = Users.query.filter((Users.email == email) | (Users.username == username)).first()
            if user is None:
                #log result
                current_app.logger.info('Username and email do not exist in db')

                #add to db
                #insert if data not found
                user_insert = Users(email=email, password=hashed_password, username=username)
                #add to db
                db.session.add(user_insert)
                #commit
                db.session.commit()

                #log data
                current_app.logger.info('Registration successful')
                msg = "Registration successful"
                return render_template('signup.html',auth_success=msg)
            else:
                #log failure
                current_app.logger.info('Registration failed. Username or email exists')
                #render failure
                error = "Registration failed. Username or email exists"
                return render_template('signup.html',auth_error=error)
        else:
            current_app.logger.info('Input validation failed')
            error = "All input is required"
            return render_template('signup.html',auth_error=error)

    return render_template('signup.html')
