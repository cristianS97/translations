#!/bin/bash
python manage.py makemigrations
python manage.py migrate
# Creación de un superusuario
DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username=admin --email=admin@admin.com --noinput
python manage.py runserver 0.0.0.0:8000