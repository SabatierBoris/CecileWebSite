#!/usr/bin/env bash

alembic -c pyramidapp/config/production.ini upgrade head
initialize_bd pyramidapp/config/production.ini
initialize_thumbnail pyramidapp/config/production.ini
gunicorn --paste pyramidapp/config/production.ini
#pserve pyramidapp/config/production.ini
