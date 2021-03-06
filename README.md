## message_board - A simple web message board

message_board is a demonstration of simple Django functionality

### Installation
 - `git clone https://github.com/kevinbowen777/message_board.git`
 - `cd message_board`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---
## Features
 - Admin user can post simple text posts

### Live Demo on Heroku:
 - [message_board live demo](https://kbowen-django-message-board.herokuapp.com/)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/message_board/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/message_board/issues)
      to view currently open bug reports or open a new issue.
