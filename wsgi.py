#!/usr/bin/env python

from pyramid.paster import get_app
import logging.config
import os, sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, 'pyramidapp'))
config = os.path.join(here, 'pyramidApp', 'config', 'production.ini')

logging.config.fileConfig(config)

application = get_app(config, 'main')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8080, application)
    server.serve_forever()
