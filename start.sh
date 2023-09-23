#!/bin/bash
cp .env.example .env

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting load data in db"
python manage.py loaddata properties.json
python manage.py loaddata advertisements.json
python manage.py loaddata reservations.json
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000
