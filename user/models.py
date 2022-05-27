# Code for various functionalities
# Importing Libraries
from flask import jsonify,request, session, redirect
from app import db, FRmodel
import uuid
from passlib.hash import pbkdf2_sha256
import joblib
from user.img_uploader import Img
from user import face_verify 

# User Class
class User:
    # Starts the user session
    def start_session(self, user):
        del user['password']
        session["logged_in"] = True
        session["user"] = user
        # print('User is:',user['name'])
        return jsonify(user), 200

    # Signup Function
    def signup(self):
        file = request.form['file']
        image_uploaded = Img.save_image(file)
        if image_uploaded:
            IMG_PATH = 'uploads/user_signup/f.jpg'
            # Converting f.jpg to respective encoding
            img_encoding = face_verify.img_to_encoding(IMG_PATH, FRmodel,uuid.uuid4().hex)
        else:
            return jsonify({"error": "Error, try again!"}), 400 

        # print('Signup_encoding:',img_encoding)

        if len(img_encoding):
            # User Details
            user = {
                "_id": uuid.uuid4().hex,
                "name": request.form.get('name'),
                "email": request.form.get('email'),
                "password": request.form.get('password'),
                "database_encoding": img_encoding
            }
            # Password is stored in database in encrypted form
            user['password'] = pbkdf2_sha256.encrypt(user['password'])
            
            # If email already exists
            if db.find_one({"email":user['email']}):
                return jsonify({"error":"Email address already registered!"}), 400
            # Else write user details in the database
            if db.insert_one(user):
                return jsonify({"sucess": "Signup successful"}), 200

        return jsonify({"error": "Error, try again!"}), 400

    # Logout Function 
    def logout(self):
        session.clear()
        return redirect('/')

    # Quick-Login Function
    def login_recog(self):
        file = request.form['file3'] 
        # Receive the uploaded image 
        login_recog_uploaded = Img.save_image(file)
        if login_recog_uploaded:
                    IMG_PATH = 'uploads/user_signup/f.jpg'
                    # Convert f.jpg into encoding
                    login_recog_encoding = face_verify.login_img_to_encoding(IMG_PATH, FRmodel)
                    # print('Login_Encoding',login_recog_encoding)
                    data = db.find()
                    # print("data= ", data)
                    # Compares login-encoding with signup-encoding and returns true if difference < 0.7
                    for user in data:
                        # To handle FileNotFoundError 
                        try:
                            fo = open(user['database_encoding'][0],"rb")
                        except FileNotFoundError:
                                continue
                        database_encoding = joblib.load(user['database_encoding'][0])
                        print('DB:',user['database_encoding'])
                        if face_verify.verify(login_recog_encoding, database_encoding):
                            return self.start_session(user)
            
                    return jsonify({"error": "Unauthorized Access "}), 401
        return jsonify({"error": "Face not found !"}), 401 





        
