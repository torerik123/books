import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    
    #book = Book(isbn=2222, title="mybook", author="Hasnsss", year="1992")    
    #db.session.add(book)
    #db.session.commit()

    for isbn, title, author, year in reader:
        if isbn or title or author or year is None:
            continue
        book = Book(isbn=isbn, title=title, author=author, year=year)
        db.session.add(book)
        #print(f"ISBN: {isbn}")
    db.session.commit()       

if __name__ == "__main__":
    with app.app_context():
        main()