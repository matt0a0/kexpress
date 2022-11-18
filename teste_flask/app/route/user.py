from flask import Blueprint,current_app,render_template, session

user = Blueprint("user",__name__)

@user.route('/')
def index():
    return "Index"

#@user.route('/login')
#def login_user():
#    return "Login"

#@user.route('/home')
#def home_user():
#    return "Home"

#@user.route('/logout')
#def logout_user():
#    return "Logout"