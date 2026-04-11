'''
Joshua Shadle
M4 Case Study: Python APIs
Purpose: Create a database with attributes you can call and observe off of a web page using
Flask.
'''

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.id} - {self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Welcome to the Book API'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher,
        }
        output.append(book_data)
    return {"books": output}

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        book_name=data['book_name'],
        author=data['author'],
        publisher=data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"id": new_book.id, "message": "Book added"})

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"message": "Book was not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book was deleted"}
