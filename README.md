# geo-data-server

The `geo-data-server` project uses Django and Django Rest Framework to create an API that works with geospatial data. This API allows you to find the nearest places to a specified point.

## Requirements

- Python 3.6+
- Django 3.0+
- Django Rest Framework
- Django REST Framework GIS
- PostgreSQL with PostGIS extension

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/juliastetsko/geo-data-server.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Start the server:
    ```bash
    python manage.py runserver
    ```

