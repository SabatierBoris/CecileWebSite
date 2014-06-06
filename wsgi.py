#!/usr/bin/env python
"""
Launch the web app in wsgi container
"""

from pyramid.paster import get_app
import logging.config
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'pyramidapp'))
CONFIG = os.path.join(HERE, 'pyramidApp', 'config', 'production.ini')

logging.config.fileConfig(CONFIG)

APPLICATION = get_app(CONFIG, 'main')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    SERVER = make_server('0.0.0.0', 8080, APPLICATION)
    SERVER.serve_forever()
