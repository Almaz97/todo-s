#!/bin/sh

echo trying to start

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
gunicorn core.wsgi:application --bind 0.0.0.0:8700
