#!/bin/bash
rm -rf rare/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations rareapi
python3 manage.py migrate rareapi
python3 manage.py loaddata category
python3 manage.py loaddata comments
python3 manage.py loaddata post
python3 manage.py loaddata users
