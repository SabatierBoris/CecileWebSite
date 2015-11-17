#!/usr/bin/env bash

alembic -c pyramidapp/config/production.ini upgrade head
initialize_bd pyramidapp/config/production.ini
pserve pyramidapp/config/production.ini
