from django.test import TestCase

from books.models import Book


class BookTestCase(TestCase):
    def setUp(self):
        pass
        # Book.objects.create(title='test book', author='test author', year='2000')

    def test_add_book(self):
        """
        Тест создания книги
        """
        data = {
            "Название": "test book",
            "Автор": "test author",
            'Год': 2000,
            "Статус": "В наличии"
        }
        add_book = Book.objects.create(title='test book', author='test author', year='2000')
        self.assertEqual(add_book, data)

    def test_book_delete(self):
        """
        Тест удаления книги
        """
        pass

    def test_list_book(self):
        """
        Тест вывода списка книг
        """
        pass

    def test_search_book(self):
        """
         Тест поиска книги
         """
        pass

    def test_change_status(self):
        """
         Тест обновления статуса книги
         """
        pass
