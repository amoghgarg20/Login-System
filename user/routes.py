# Routes
# Importing Libraries
from flask import render_template
from app import app
from user.models import User
from user.img_uploader import Img

@app.route('/user/signup', methods=["POST"])
def signup():
    return User().signup()

@app.route('/user/logout')
def logout():
    return User().logout()

@app.route('/user/login-recog', methods=['POST'])
def login_recog():
    return User().login_recog()

@app.route('/user/signup', methods=["GET"])
def signup_get():
    return render_template("signup.html")

@app.route('/user/login-recog', methods=['GET'])
def login_recog_get():
    return render_template("quicklogin.html")




