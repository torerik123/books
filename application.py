from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
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
        return render_template("index.html", allbooks=allbooks, navbar=False)

    else:
        # Get selected book
        selected = request.form.get("book_list")

        if selected != "":
            return redirect(url_for('results', search = selected))   
            
        # If no matches
        else:
            return redirect(url_for('results', search = selected))

@app.route("/results/<string:search>")
def results(search):

    #Title
        title_lookup = Book.query.filter(Book.title.ilike('%' + search + '%')).all()
        title_results = []

        for result in title_lookup:
            title_results.append(result)
    
        # Author 
        author_lookup = Book.query.filter(Book.author.ilike('%' + search + '%')).all()
        author_results = []

        for result in author_lookup:
            author_results.append(result)

       # ISBN
        isbn_lookup = Book.query.filter(Book.isbn.ilike('%' + search + '%')).all()
        isbn_results = []

        for result in isbn_lookup:
            isbn_results.append(result)   
               
        return render_template("results.html", navbar=True, title_results=title_results, author_results=author_results, isbn_results=isbn_results, search=search)
        

@app.route("/reviews/<string:isbn>")
def reviews(isbn):
    """ Call to Goodreads API for reviews"""
    
    # Reviews
    res = requests.get(f"https://www.goodreads.com/book/isbn/{isbn}?format=json&user_id=122566280") 
    
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful")
    
    data = res.json()
    
    return data        


@app.route("/book/<string:isbn>")
def book(isbn):
    """ Lookup book by isbn """ 
         
    isbn_lookup = Book.query.filter(Book.isbn.like('%' + str(isbn) + '%')).all()
    isbn_results = []

    for result in isbn_lookup:
            isbn_results.append(result)

    # If more than 1 results, return search page
    if len(isbn_lookup) > 1:
        return render_template("results.html", navbar = True, isbn_results=isbn_results)
            
    # Show book info
    else: 
                
        title = result.title
        author = result.author
        year = result.year
        isbn = result.isbn

        # Review widget from Goodreads API
        response = reviews(isbn)

        content = str(response['reviews_widget'])

        #CSS
        style_section = content.split("</style>")[0] + "</style>"
        
        # Reviews
        content_section = content.split("</style>")[1]

        return render_template("book.html",navbar = True, title=title, author=author, year=year, isbn=isbn, content_section=content_section, style_section=style_section)


     
        