#!/bin/bash 

python src/core/manage.py makemigrations --no-input
python src/core/manage.py migrate --no-input

python src/core/manage.py runserver 0.0.0.0:8000