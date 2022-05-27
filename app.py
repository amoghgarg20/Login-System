# app.py
# Importing Libraries
from flask import Flask, render_template, redirect, session
import pymongo
from functools import wraps
from user import face_verify 

# Initialising the app
app = Flask(__name__)
# Any random string
app.secret_key = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

# Connecting with Mogodb(Database)
# MongoDB URI
mongoURI ='mongodb+srv://amoghgarg9:vasu20@cluster0.dm6fi.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(mongoURI)
database = client.get_database('flask_user_data1')
db = database.flask_user_login_data

# Loads the facenet model into 'FRmodel' variable
FRmodel = face_verify.load_model()

# Login required
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/user/login-recog')
  return wrap

#Routes
from user import routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template("afterlogin.html")

