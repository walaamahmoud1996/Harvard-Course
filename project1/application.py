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

@app.route("/registration")
def registraion():
    return render_template("registration.html")

@app.route("/register",methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    db.execute("INSERT INTO SystemUsers(username,password) VALUES(:username,:password)",
    {"username":username,"password":password})
    db.commit()
    return render_template("success.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/checkAuth")
def checkAuth():

    username = request.form.get("username")
    password = request.form.get("password")
    if db.execute("SELECT * FROM SystemUsers WHERE username=:username AND password=:password",{'username':username ,'password':password}).rowcount ==0:
        return render_template("error.html",message = "Wrong username or password")
    return render_template("Welcome.html",User="username")
