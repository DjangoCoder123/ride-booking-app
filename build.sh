#!/usr/bin/env bash
# exit on error
set -o errexit

# Install all software requirements
pip install -r requirements.txt

# Clear and compile your static web files
python manage.py collectstatic --noinput

# Force compile and apply the missing database tables layout
python manage.py makemigrations UberApp
python manage.py migrate
