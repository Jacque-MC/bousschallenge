#!/bin/bash

cd /app/bouschallenge

python manage.py migrate

exec "$@"