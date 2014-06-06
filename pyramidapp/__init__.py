"""
__init__ file of the pyramid application
Contain the main function
"""
from pyramid.config import Configurator
from pyramid.response import Response


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

    config = Configurator(settings=settings)

    config.add_view(hello_world)

    return config.make_wsgi_app()
