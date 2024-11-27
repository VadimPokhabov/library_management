# Приложение "Library Management" система управление библиотекой
---
Приложение выполнено на Django

### Стек

* Django
* psycopg2 (ORM)

___
Для запуска проекта у себя локально необходимо:

1. git clone репозитория

```
git@github.com:VadimPokhabov/library_management.git
```

2. Установить виртуальное окружение venv

```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```

3. Активировать виртуальное окружение

```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```

4. установить файл с зависимостями

```
pip install -r requirements.txt
```

5. Создать базу данных в PgAdmin, либо через терминал. Необходимо дать название в файле settings.py в каталоге 
   'library_management' в константе (словаре) 'DATABASES'
6. Заполнить своими данными файл .env в корне вашего проекта. Образец файла лежит в корне .env.sample
7. Для запуска проекта использовать команду

```
python manage.py ruserver
```

Запуск приложения через Docker:

1. Повторить шаги 1-3
2. Запустить Docker локально на машине
3. Выполнить команду в терминале

```
docker compose up -d --build
```

Данная команда сразу создаст образ, и сбилдит его, т.е. запустит локально в Docker

4. Переходим по ссылке http://localhost:8000/  


Чтобы удалить контейнеры после работы с приложением используйте команду

```
docker-compose down
```

----
Данное приложение работает через консоль  
Пользователю доступны следующие команды:

1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id
   и статусом “в наличии”.

```commandline
python manage.py library_command add
```

2. Удаление книги: Пользователь вводит idкниги, которую нужно удалить.

```commandline
python manage.py library_command delete
```

3. Поиск книги: Пользователь может искать книги по title, author или year.

```commandline
python manage.py library_command search
```

4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.

```commandline
python manage.py library_command list
```

5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

```commandline
python manage.py library_command change_status
```

___
Дополнительно:

* Реализовано хранение данных в текстовом или json формате.
* Обеспечена корректная обработка ошибок (например, попытка удалить несуществующую книгу).
* Написаны функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
* Не использованы сторонние библиотеки.