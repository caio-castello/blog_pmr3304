#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install gunicorn psycopg2

python manage.py collectstatic --no-input