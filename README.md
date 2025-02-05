# Социальная сеть "Блогикум" (RU)

Описание проекта
---
Проект представляет собой блог-платформу на Django. В нем реализованы ключевые функции: создание и отображение публикаций, страницы постов, категории, а также настройка админ-зоны для управления контентом.

Основные задачи
---
✔️ Создание моделей (Post, Category, Location)  
✔️ Реализация представлений для отображения данных  
✔️ Подключение шаблонов и статики  
✔️ Настройка панели администратора с русской локализацией

Стек технологий
---
- Python 3.9
- Django 3.2
- HTML, CSS

Установка проекта из репозитория (Windows)
---
1. Клонировать репозиторий:
```bash
git clone git@github.com:JarexTI/django_sprint3.git
```
2. Создать и активировать виртуальное окружение:
```bash
python -m venv venv

source venv/Scripts/activate
```
3. Установить зависимости из файла `requirements.txt`:
```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции
```
python blogicum/manage.py migrate
```
5. Загрузить фикстуры DB
```
python blogicum/manage.py loaddata db.json
```
6. Создать суперпользователя
```
python blogicum/manage.py createsuperuser
```
7. Запустить проект:
```bash
python blogicum/manage.py runserver
```
8. Переходим на сервер разработки:
```bash
http://127.0.0.1:8000/
```
<br>

# Social Network "Blogicum" (EN)

Project Description
---
This project is a blog platform built with Django. It includes key features such as creating and displaying posts, post detail pages, categories, and setting up an admin panel for content management.

Key Tasks
---
✔️ Creating models (Post, Category, Location)  
✔️ Implementing views to display data  
✔️ Connecting templates and static files  
✔️ Setting up an admin panel with Russian localization

Technology Stack
---
- Python 3.9
- Django 3.2
- HTML, CSS

Installation from Repository (Windows)
---
1. Clone the repository:

```bash
git clone git@github.com:JarexTI/django_sprint3.git
```

2. Create and activate the virtual environment:

```bash
python -m venv venv

source venv/Scripts/activate
```

3. Install dependencies from the `requirements.txt` file:

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Run migrations:

```
python blogicum/manage.py migrate
```

5. Load the DB fixtures:

```
python blogicum/manage.py loaddata db.json
```

6. Create a superuser:

```
python blogicum/manage.py createsuperuser
```

7. Run the project:

```bash
python blogicum/manage.py runserver
```

8. Open the development server:

```bash
http://127.0.0.1:8000/
```
