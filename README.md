# Book Review API
Libretto Luminary is a book review website built with Django and Django Rest Framework. It allows users to read reviews.

### Features

Browse a collection of books

Read detailed book information and reviews

API endpoints for books and reviews

Server-side rendered pages with Bootstrap for styling

### Technology Stack

Django

Django Rest Framework

Bootstrap

SQLite (for development)

#### Installation

#### Clone the repository:

**git clone https://github.com/yourusername/libretto-luminary.git**

**cd libretto-luminary**

#### Create a virtual environment and activate it:

**py -m venv venv**

**source venv/bin/activate**  # On Windows use `venv\Scripts\activate`

#### Install the required packages:

**pip install -r requirements.txt**

#### Run migrations:

**py manage.py migrate**

#### Create a superuser:

**py manage.py createsuperuser**

#### Run the development server:

**py manage.py runserver**

**Visit http://127.0.0.1:8000/admin/ to add books and reviews.**

#### Usage

Browse books: Visit http://127.0.0.1:8000/

API endpoints:

Books: http://127.0.0.1:8000/api/books/

Reviews: http://127.0.0.1:8000/api/reviews/
