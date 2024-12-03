from django.db import models


class Book(models.Model):
    """Класс модели книг"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    status = models.CharField(max_length=20, default='В наличии')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        constraints = [
            models.UniqueConstraint(fields=['title', 'author', 'year'], name='name of constraint')
        ]

    def __str__(self):
        return f'Название: {self.title}, \nАвтор: {self.author}, \nГод{self.year}, \nСтатус: {self.status}'
