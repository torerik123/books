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

    if request.method == "GET":
        allbooks = Book.query.all()
        return render_template("index.html", allbooks=allbooks)

    else:

        # Get selected book
        selected = request.form.get("book_list")

        # Lookup in database
        lookup = Book.query.filter_by(title=selected).first()
        #lookup = Book.query.filter_by(title=selected).all()


        ## add some logic to get all titles in selected
        #results = []

        #for result in lookup:
        #    results.append(result.title)
        
        # if more than 1 results

           # If not found: ???

        title = lookup.title
        author = lookup.author
        year = lookup.year
        isbn = lookup.isbn

        return render_template("book.html", title=title, author=author, year=year, isbn=isbn)

     
        