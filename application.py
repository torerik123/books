from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp
import os
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():

    #if request.method == "GET":
    allbooks = Book.query.all()
        #print(allbooks)
    
    #else:
        # Go to selected book page

    return render_template("index.html", allbooks=allbooks)