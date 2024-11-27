import json


def save_books_to_file(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)


def load_books_from_file():
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []
