from django.core.management.base import BaseCommand
from books.views import add_book, delete_book, search_book, list_books, change_status


class Command(BaseCommand):
    """Управление библиотекой книг"""
    help = 'Управление библиотекой книг'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)

    def handle(self, *args, **options):
        action = options['action']

        if action == 'add':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            add_book(title, author, year)
        elif action == 'delete':
            book_id = int(input("Введите ID книги для удаления: "))
            delete_book(book_id)
        elif action == 'search':
            query = input("Введите запрос для поиска: ")
            books = search_book(query)
            for book in books:
                print(f"Найдена книга: {book.title} ({book.author}, {book.year})")
        elif action == 'list':
            list_books()
        elif action == 'change_status':
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            change_status(book_id, new_status)
