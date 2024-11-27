from books.models import Book


def add_book(title, author, year):
    book = Book(title=title, author=author, year=year)
    book.save()


def delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
    except Book.DoesNotExist:
        print("Книга с таким id не найдена")


def search_book(query):
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(
        author__icontains=query) | Book.objects.filter(year=query)
    return books


def list_books():
    books = Book.objects.all()
    for book in books:
        print (f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
               f"Год издания: {book.year}, Статус: {book.status}")


def change_status(book_id, new_status):
    try:
        book = Book.objects.get(id=book_id)
        book.status = new_status
        book.save()
    except Book.DoesNotExist:
        print("Книга с таким id не найдена")
