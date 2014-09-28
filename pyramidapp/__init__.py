# coding : utf-8
"""
__init__ file of the pyramid application
Contain the main function
"""
from pyramid.config import Configurator
from pyramid.response import Response

from sqlalchemy import engine_from_config

from .models import DB_SESSION, BASE


def hello_world(request):
    """
    Example of a request function
    """
    request = request  # Remove W0613
    return Response('Hello!')


def main(global_config, **settings):
    """
    This function returns a WSGI application.
    """
    global_config = global_config  # Remove W0613

    engine = engine_from_config(settings, 'sqlalchemy.')
    DB_SESSION.configure(bind=engine)
    BASE.metadata.bind = engine

    config = Configurator(settings=settings)

    config.add_view(hello_world)

    return config.make_wsgi_app()
