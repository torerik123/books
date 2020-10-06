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
       

        
        

     
        