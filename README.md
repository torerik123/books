# Find book reviews by title, author or ISBN number

# Demo

[Demo](https://tor-books.herokuapp.com/)

# APIS used

- NY times to show best selling books on the front page
- Google books to show book covers, ratings and book descriptions
- Goodreads to show book reviews


# Technology

Front-end: 
    - HTML
    - CSS
    - Javascript

Back-end:
    - Python
    - Flask
    - Postgres


# What I learned making this
I built this project to learn more about object-oriented programming and using different APIs to display data.
This was also my first time using Postgres with SQLalchemy ORM. The majority of the site is made with Bootstrap components with a few tweaks.


# How it works

## Index

### Bestsellers
The index page shows the top books from the NY times bestseller list. 
Using Javascript, the ISBN numbers of the best selling books are fetched from the NY Times API. Then the book covers, title and author names are fetched from Google books and inserted into the corresponding cards.

(The books displayed on the front page are currently not in the database, so they won't show up in a search)

### Search
When typing in text in the search bar the user will see suggestions as they are typing.
The database only contains 5000 books, so not all books will be available in a search. 
I could have only used Goodreads API or Google books for the search function and have more books available,
but I wanted to get more experience with Postgres and SQLalchemy.


## Results
The results page will show all results for a given ISBN, author or title. Partial matches will also show up. 
There is no option to sort the search results at the moment, but I might add that in the future.
As it is right now, the search page will show titles first, then authors, then ISBNs if there are any matches.
Clicking an author name will only show books by that author.

## Book info
The book info page displays the rating and description from Google books.
The reviews are pulled from Goodreads and displayed in a widget.


# How to run

models.py - Creates tables in database
import.py - Imports books.csv to the database

- set FLASK_APP=application.py
- set DATABASE_URL = [postgres db]
- flask run
