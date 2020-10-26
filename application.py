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
def search():

    if request.method == "GET":
        allbooks = Book.query.all()
        return render_template("index.html", allbooks=allbooks)

    else:
        # Get selected book
        selected = request.form.get("book_list")

        if selected != "":
        # Lookup in database, ignores case
            
            #TODO: Make functions
            #Title
            title_lookup = Book.query.filter(Book.title.ilike('%' + selected + '%')).all()
            title_results = []

            for result in title_lookup:
                title_results.append(result)
            
            # Author 
            # TODO: Only get unique results
            author_lookup = Book.query.filter(Book.author.ilike('%' + selected + '%')).all()
            author_results = []

            for result in author_lookup:
                author_results.append(result)

            # ISBN
            isbn_lookup = Book.query.filter(Book.isbn.ilike('%' + selected + '%')).all()
            isbn_results = []

            for result in isbn_lookup:
                isbn_results.append(result)   
               
            return render_template("results.html", title_results=title_results, author_results=author_results, isbn_results=isbn_results)

        else:
            return render_template("results.html")


@app.route("/results/<search>")
def results(search):

    # TODO: Correct title,author, isbn, search
    if search != "":
        
        #Title
        title_lookup = Book.query.filter(Book.title.ilike('%' + search + '%')).all()
        title_results = []

        for result in title_lookup:
            title_results.append(result)
    
        if len(title_results) > 1:    
            return render_template("results.html", title_results=title_results)
        else:

            return redirect(url_for('book', isbn=isbn))
    else:
        return "No matches"
    

@app.route("/reviews/<int:isbn>")
def reviews(isbn):
    """ Call to Goodreads API for reviews"""
    
    # Reviews
    res = requests.get("https://www.goodreads.com/book/isbn/ISBN?format=json", params={"key": "zID72O5cas5E9C4byZW1w", "isbn": isbn })

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful")
    
    data = res.json()
    
    return data        


@app.route("/book/<string:isbn>")
def book(isbn):
    """ Lookup book by isbn """ 
         
    lookup = Book.query.filter(Book.isbn.like('%' + str(isbn) + '%')).all()
    results = []

    for result in lookup:
            results.append(result)

    # If more than 1 results, return search page
    if len(lookup) > 1:
        return render_template("results.html", results=results)
            
    # Show book info
    else: 
                
        title = result.title
        author = result.author
        year = result.year
        isbn = result.isbn


        # Goodreads review widget
        response = reviews(isbn)

        content = str(response['reviews_widget'])

        #CSS
        style_section = content.split("</style>")[0] + "</style>"
        
        # Reviews
        content_section = content.split("</style>")[1]

        return render_template("book.html", title=title, author=author, year=year, isbn=isbn, content_section=content_section, style_section=style_section)




        
        

     
        