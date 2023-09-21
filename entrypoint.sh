#!/bin/sh

poetry run python manage.py makemigrations
poetry run python manage.py migratedocker images -a
poetry run gunicorn core.wsgi:application --bind 0.0.0.0:8000
