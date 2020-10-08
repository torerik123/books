from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from tempfile import mkdtemp
import os
import requests
from models import *
import json

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

        if selected != "":
            # Lookup in database, ignores case
            lookup = Book.query.filter(Book.title.ilike('%' + selected + '%')).all()
            results = []

                # TODO: If more than 1 rows
            for result in lookup:
                results.append(result)

            if len(results) > 1:    
                return render_template("results.html", results=results)
            else:
                title = result.title
                author = result.author
                year = result.year
                isbn = result.isbn

                return render_template("book.html", title=title, author=author, year=year, isbn=isbn)

        else:
            return "No matches"


@app.route("/get_book/<int:isbn>")
def get_book(isbn):
    """ Call to Goodreads API"""
    
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "zID72O5cas5E9C4byZW1w", "isbns": isbn })
    
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful")
    
    data = res.json()
    return str(data)   

        
        

     
        