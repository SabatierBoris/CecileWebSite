#!/usr/bin/env bash

alembic -c pyramidapp/config/production.ini upgrade head
initialize_bd pyramidapp/config/production.ini
gunicorn -w 16 -b 0.0.0.0:8080 wsgi
#pserve pyramidapp/config/production.ini
