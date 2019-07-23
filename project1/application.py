import os

from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "TO DO MAN"

@app.route("/Signup",methods=["GET","POST"])
def Signup():
    message = None
    if request.method =="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if db.execute("SELECT username FROM SystemUsers WHERE username=:username",{"username":username}).rowcount==0:
            db.execute("INSERT INTO SystemUsers(username,password) VALUES(:username,:password)",{"username":username,"password":password})
            message = "your registration was Successful"
        else:
            message="username already in use"
        db.commit()
    return render_template("Signup.html",message= message)

@app.route("/login",methods=["GET","POST"])
def login():
    message =None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "" or password =="":#handle this case later in html
            return render_template("error.html",message="you must fill both fields")
        else:
            if db.execute("SELECT * FROM SystemUsers WHERE username=:username AND password =:password",{"username":username,"password":password}).rowcount==0:
                message="Wrong username or password"
            else:
                return render_template("Welcome.html",User=username)
            db.commit()

    return render_template("login.html",message=message)
