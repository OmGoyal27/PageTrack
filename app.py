
import json
import os
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)
BOOKS_FILE = os.path.join(os.path.dirname(__file__), 'database', 'books.json')

def load_books():
    with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=2, ensure_ascii=False)




@app.route('/')
def index():
    books = load_books()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        books = load_books()
        isbn = request.form.get('isbn', '').strip()
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        description = request.form['description']
        new_id = max([b['id'] for b in books], default=0) + 1 if books else 1
        new_book = {
            'id': new_id,
            'isbn': isbn,
            'title': title,
            'author': author,
            'year': year,
            'description': description
        }
        books.append(new_book)
        save_books(books)
        return redirect(url_for('index'))
    return render_template('add_book.html')


@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    books = load_books()
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return "Book not found", 404
    if request.method == 'POST':
        book['isbn'] = request.form.get('isbn', '').strip()
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['year'] = request.form['year']
        book['description'] = request.form['description']
        save_books(books)
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)
@app.route('/api/fetch_book_info')
def fetch_book_info():
    isbn = request.args.get('isbn', '').strip()
    if not isbn:
        return jsonify({'error': 'No ISBN provided'}), 400
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    resp = requests.get(url)
    if resp.status_code != 200:
        return jsonify({'error': 'Failed to fetch from Google Books'}), 500
    data = resp.json()
    if 'items' not in data or not data['items']:
        return jsonify({'error': 'No book found for this ISBN'}), 404
    info = data['items'][0]['volumeInfo']
    return jsonify({
        'title': info.get('title', ''),
        'author': ', '.join(info.get('authors', [])),
        'year': info.get('publishedDate', '')[:4],
        'description': info.get('description', '')
    })


@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    books = load_books()
    new_books = [b for b in books if b['id'] != book_id]
    save_books(new_books)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
