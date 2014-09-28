#!/bin/sh

#pip install pep8 > /dev/null
#pip install pylint > /dev/null
#pip install nose > /dev/null
#python setup.py develop --upgrade > /dev/null

set -e

pep8 pyramidapp setup.py wsgi.py
#pylint pyramidapp setup.py wsgi.py
nosetests
initialize_bd pyramidapp/config/development.ini
pserve pyramidapp/config/development.ini --reload
