#!/bin/bash

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 1
done
echo "MySQL started"

python manage.py makemigrations
python manage.py migrate

exec "$@"